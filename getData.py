import requests
import string
import random
import json
import tree
import re
import map 
import time
import os

classesWithPrereqs = []

def getUfData():
    all_data = []
    session = requests.Session()
    break_flag = False
    last_row = 0
    while True:
        response = session.get(f'https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number={last_row}') 
        data = json.loads(response.text)
        courses = data[0]['COURSES']
        for course in courses:
            code = course.get('code', '0000')
            if code == '0000':
                break_flag = True
                break
            print(course)
            all_data.append(course)
        if break_flag:
            break
        last_row += len(courses)
        print(len(all_data))

    with open('all_data.json', 'w') as f:
        json.dump(all_data, f)

def populateUfData(tree_obj, map_obj):
    with open('all_data.json', 'r') as f:
        all_Courses = json.load(f)

    for course in all_Courses:
        code = course.get('code')
        name = course.get('name')
        prerequisites = course.get('prerequisites')        
        preReqs = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
        preReqs = [prereq.replace(" ", "") for prereq in preReqs if prereq.replace(" ", "") != code]

        # ADD THIS FOR RANDOMLY GENERATED DATA
        if preReqs and code not in classesWithPrereqs:
            classesWithPrereqs.append(code)
        
        tree_obj.insert(code, preReqs)
        map_obj.insert(code, preReqs)

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def getRandomClass():
    return random.choice(classesWithPrereqs)

def generate_course_code():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    return letters + numbers

def create_additional_courses(num_courses=100000):
    # create each course, generating a unique code, and adding the course with no pre-requisites
    new_courses = []
    for i in range(num_courses): 
        course_code = generate_course_code()  
        new_courses.append({"code": course_code, "prerequisites": []})  
    return new_courses

def assign_prerequisites(courses):
    # selecting a 1/3 of the courses randomly, getting the other 2/3s of the courses 
    # randomly selecting those pre-reqs 
    # and then setting the pre-rqs to each course
    third_courses = random.sample(courses, len(courses) // 3) 
    other_courses = [course for course in courses if course not in third_courses]  

    for course in third_courses:
        num_prereqs = random.randint(0, 3)  
        prereqs = random.sample(other_courses, num_prereqs) 
        course['prerequisites'] = [prereq['code'] for prereq in prereqs if prereq['code'] != course['code']]

    return courses

def generateRandomData(limit=100000):
    all_courses = []
    new_courses = create_additional_courses()
        
        # Assign prerequisites only to the new courses
    new_courses_with_prereqs = assign_prerequisites(new_courses)

        # Combine with existing courses
    all_courses.extend(new_courses_with_prereqs)

    with open('randomlyGeneratedCourses.json', 'w') as file:
        json.dump(all_courses, file, indent=4)

    print(f"Total courses after update: {len(all_courses)}")

def populateRandomData(tree_obj, map_obj):
    with open('randomlyGeneratedCourses.json', 'r') as f:
        all_Courses = json.load(f)

    for course in all_Courses:
        code = course.get('code')
        prerequisites = course.get('prerequisites')        

        if prerequisites and code not in classesWithPrereqs:
            classesWithPrereqs.append(code)
        
        tree_obj.insert(code, prerequisites)
        map_obj.insert(code, prerequisites)
