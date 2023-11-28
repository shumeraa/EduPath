import requests
import json
import pickle

with open('classMap.pkl', 'rb') as f:
    classMap = pickle.load(f)


print(classMap['AEB3510'])

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
