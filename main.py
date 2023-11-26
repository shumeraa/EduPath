import requests
import json


classMap = {}
#stores course code, course ID, course name, prerequisites

#Spring 2024 class schedule, first 50 classes
response = requests.get('https://one.ufl.edu/apix/soc/schedule/?category=CWSP&term=2241&last-control-number=0') 
data = json.loads(response.text)

courses = data[0]['COURSES']
for course in courses:
    code = course.get('code', 'Unknown Code')
    courseId = course.get('courseId', 'Unknown ID')
    name = course.get('name', 'Unknown Name')
    prerequisites = course.get('prerequisites', 'No Prerequisites')
    classMap[code] = [courseId, name, prerequisites]
    #print(courseCode, courseID, courseName, prereqs)

x = classMap['ABE3212C']
print(x)


# for i in range(50):
#     courseCode = data[i]['code']
#     courseID = data[i]['courseId']
#     courseName = data[i]['name']
#     prereqs = data[i]['prerequisites']
#     #classMap[courseCode] = [courseID, courseName, prereqs]
#     print(courseCode, courseID, courseName, prereqs)



