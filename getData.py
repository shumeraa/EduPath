import requests
import string
import random
import json




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


getUfData()



