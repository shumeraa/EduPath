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