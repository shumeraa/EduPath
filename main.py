import requests
import json


classMap = {}
#stores course code, course ID, course name, prerequisites
last_row = 0
session = requests.Session()

#Spring 2024 class schedule, first 50 classes
while True:
    response = session.get(f'https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number={last_row}') 
    data = json.loads(response.text)

    courses = data[0]['COURSES']
    for course in courses:
        code = course.get('code', 'Unknown Code')
        courseId = course.get('courseId', 'Unknown ID')
        name = course.get('name', 'Unknown Name')
        prerequisites = course.get('prerequisites', 'No Prerequisites')
        classMap[code] = [courseId, name, prerequisites]
        if code == '0000':
            break         

    last_row += len(courses)
    print(last_row)




