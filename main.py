import json

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

classMap = {}

count = 0

for course in all_Courses:
    print(count)
    count += 1

    # name = course.get('name')
    # print(name)
    # sections = course.get('sections')
    # for section in sections:
    #     classNumber = section.get('classNumber')
    #     print(classNumber)

print(count)