import json
import random
import string
import main

# def generate_course_code():
#     letters = ''.join(random.choices(string.ascii_uppercase, k=3))
#     numbers = ''.join(random.choices(string.digits, k=4))
#     return letters + numbers

# def generate_prerequisites(num_prereqs=3):
#     prerequisites = []
#     for i in range(num_prereqs):
#         prerequisites.append(generate_course_code())
#     return prerequisites

# def create_additional_courses(num_courses=90000):
#     new_courses = []
#     for j in range(num_courses):
#         course_code = generate_course_code()
#         prereqs = generate_prerequisites(random.randint(0, 5)) 
#         new_courses.append({"code": course_code, "prerequisites": prereqs})
#     return new_courses

# def create_additional_courses_up_to_limit(num_courses=90000, limit=100000):
#     with open('all_data.json', 'r') as file:
#         existing_courses = json.load(file)

#     current_course_count = len(existing_courses)
#     if current_course_count >= limit:
#         print(f"The dataset already has {current_course_count} courses.")
#         return existing_courses

#     courses_to_add = limit - current_course_count
#     print(f"Adding {courses_to_add} courses to reach the limit of {limit}.")

#     new_courses = create_additional_courses(courses_to_add)

#     all_courses = existing_courses + new_courses

#     with open('all_data.json', 'w') as file:
#         json.dump(all_courses, file, indent=4)

#     return all_courses

# all_courses = create_additional_courses_up_to_limit()


# print(f"Total courses in the updated dataset: {len(all_courses)}")


###################################################
############# UPDATED CODE ########################
###################################################

# same function as before generate 3 random letters and 4 random numbers
def generate_course_code():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    return letters + numbers

# also same function as before, create each course, generating a unique code, and adding the course with no pre-requisites
def create_additional_courses(num_courses=100000):
    new_courses = []
    for i in range(num_courses): 
        course_code = generate_course_code()  
        new_courses.append({"code": course_code, "prerequisites": []})  
    return new_courses

# selecting a 1/3 of the courses randomly, getting the other 2/3s of the courses 
# randomly selecting those pre-reqs 
# and then setting the pre-rqs to each course
def assign_prerequisites(courses):
    third_courses = random.sample(courses, len(courses) // 3) 
    other_courses = [course for course in courses if course not in third_courses]  

    for course in third_courses:
        num_prereqs = random.randint(0, 3)  
        prereqs = random.sample(other_courses, num_prereqs) 
        course['prerequisites'] = [prereq['code'] for prereq in prereqs if prereq['code'] != course['code']]

    return courses

def update_course_data(limit=100000):
    all_courses = []
    new_courses = create_additional_courses()
        
        # Assign prerequisites only to the new courses
    new_courses_with_prereqs = assign_prerequisites(new_courses)

        # Combine with existing courses
    all_courses.extend(new_courses_with_prereqs)

    with open('updated_courses_data.json', 'w') as file:
        json.dump(all_courses, file, indent=4)

    print(f"Total courses after update: {len(all_courses)}")

update_course_data()