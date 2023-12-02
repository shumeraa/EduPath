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
def print_prerequisites_tree(course, level=0):
    indent = "  " * level
    prereqs = tree_obj.get_vector(course)

    # Check if the prerequisites list is empty or contains 'None'
    if not prereqs or prereqs == [None]:
        #print(f"{indent}No prerequisites for {course}")
        return
    
    #print(f"{indent}Prerequisites for {course}: {prereqs}")

    # Iterate through the prerequisites
    for prereq in prereqs:
        # If the prerequisite is not 'None', recursively print its prerequisites
        if prereq is not None:
            print_prerequisites_tree(prereq, level + 1)

def print_prerequisites_map(course, level=0):
    indent = "  " * level
    prereqs = map_obj.get_prereqs(course)

    # Check if the prerequisites list is empty or contains 'None'
    if not prereqs or prereqs == [None]:
        #print(f"{indent}No prerequisites for {course}")
        return
    
    #print(f"{indent}Prerequisites for {course}: {prereqs}")

    # Iterate through the prerequisites
    for prereq in prereqs:
        # If the prerequisite is not 'None', recursively print its prerequisites
        if prereq is not None:
            print_prerequisites_map(prereq, level + 1)


# treeStartTime = time.perf_counter()
# print_prerequisites_tree("COP3530")
# treeEndTime = time.perf_counter()
# print(f"tree is {treeEndTime - treeStartTime}")

# mapStartTime = time.perf_counter()
# print_prerequisites_map("COP3530")
# mapEndTime = time.perf_counter()
# print(f"map is {mapEndTime - mapStartTime}")

# print((treeEndTime - treeStartTime) > (mapEndTime - mapStartTime))

tree_obj.displayPreReqGraph("COP3530", draw=True)
map_obj.displayPreReqGraph("COP3530", draw=True)








