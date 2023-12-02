import json
import tree
import re
import map as hashMap
import time


with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

tree_obj = tree.classTree()
map_obj = hashMap.HashMap()

for course in all_Courses:
    code = course.get('code')
    name = course.get('name')
    prerequisites = course.get('prerequisites')        

    preReqs = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
    preReqs = [prereq.replace(" ", "") for prereq in preReqs if prereq.replace(" ", "") != code]

    tree_obj.insert(code, preReqs)
    map_obj.insert(code, preReqs)
    
        



#main function
def print_prerequisites(course, level=0):
    indent = "  " * level
    prereqs = tree_obj.get_vector(course)

    # Check if the prerequisites list is empty or contains 'None'
    if not prereqs or prereqs == [None]:
        print(f"{indent}No prerequisites for {course}")
        return
    
    print(f"{indent}Prerequisites for {course}: {prereqs}")

    # Iterate through the prerequisites
    for prereq in prereqs:
        # If the prerequisite is not 'None', recursively print its prerequisites
        if prereq is not None:
            print_prerequisites(prereq, level + 1)


#print_prerequisites("COP3530")
tree_obj.displayPreReqGraph("COP3530", draw=True)


# start_time = time.time()
map_obj.displayPreReqGraph("COP3530", draw=True)
# end_time = time.time()
# print(f"map time: {end_time - start_time} seconds")







