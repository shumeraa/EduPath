import requests
import json
import pickle

all_data = []
all_data.append("[{\"COURSES\":")
session = requests.Session()
break_flag = False
last_row = 0



while True:
    response = session.get(f'https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number={last_row}') 
    data = json.loads(response.text)
    courses = data[0]['COURSES']
    for course in courses:
        code = course.get('code', '0000')
        if code == '0000' or last_row > 300:
            break_flag = True
            break
        print(course)
        all_data.append(course)
    if break_flag:
         break
    last_row += len(courses)
    print(len(all_data))


all_data.append("}]")
with open('all_data.json', 'w') as f:
    json.dump(all_data, f)


# classMap = {}
# stores course code, course ID, course name, prerequisites
# last_row = 0
# session = requests.Session()
# departments = set()
# break_flag = False

#Spring 2024 class schedule, first 50 classes
# while True:
#     response = session.get(f'https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number={last_row}') 
#     data = json.loads(response.text)
#     courses = data[0]['COURSES']
#     for course in courses:
#         code = course.get('code', 'Unknown Code')
#         if code == '0000':
#             break_flag = True
#             break
#         courseId = course.get('courseId', 'Unknown ID')
#         name = course.get('name', 'Unknown Name')
#         prerequisites = course.get('prerequisites')
#         sectionsVector = 
#         sections = course.get('sections')
#         for section in sections:
#             classNumber = section.get('classNumber')
#             key = f"{code}_{courseId}_{classNumber}"
#             classMap[key] = [name, prerequisites]
#             print(key)
#         #deptName = course.get('sections')[0].get('deptName')
        
                 
        
#     if break_flag:
#         break
#     last_row += len(courses)
#     print(len(classMap))

# with open('classMap.json', 'w') as f:
#     json.dump(classMap, f)




