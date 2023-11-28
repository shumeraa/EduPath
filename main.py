import requests
import json

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

classMap = {}

while True:
    courses = all_Courses['COURSES']
    for course in courses:
        name = course.get('name')
        print(name)
        sections = course.get('sections')
        for section in sections:
            classNumber = section.get('classNumber')
            print(classNumber)
