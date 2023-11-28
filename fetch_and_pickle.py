import requests
import json
import pickle



classMap = {}
#stores course code, course ID, course name, prerequisites
last_row = 0
session = requests.Session()
departments = set()
break_flag = False


#Spring 2024 class schedule, first 50 classes
while True:
    response = session.get(f'https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number={last_row}') 
    data = json.loads(response.text)
    courses = data[0]['COURSES']
    for course in courses:
        if code == '0000':
            break_flag = True
            break
        code = course.get('code', 'Unknown Code')
        courseId = course.get('courseId', 'Unknown ID')
        name = course.get('name', 'Unknown Name')
        prerequisites = course.get('prerequisites', 'No Prerequisites')
        #deptName = course.get('sections')[0].get('deptName')
        classMap[code] = [courseId, name, prerequisites]
        print(code)
                 
        
    if break_flag:
        break
    last_row += len(courses)
    print(len(classMap))

with open('classMap.pkl', 'wb') as f:
    pickle.dump(classMap, f)




