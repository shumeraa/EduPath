import json
import tree
import re
import hashMap
import time
# from treelib import Node, Tree

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

tree_obj = tree.classTree()
map_obj = hashMap.HashMap()

for course in all_Courses:
    code = course.get('code')
    name = course.get('name')
    prerequisites = course.get('prerequisites')


    if "AP credit for" not in prerequisites:
        preReqs = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
        preReqs = [code.replace(" ", "") for code in preReqs]
    

    # if re.search(r'\b(AP|IBA)\b', prerequisites):

    tree_obj.insert(code, preReqs)
    # print(preReqs)
    # print(prerequisites)
    if code == "MAC2311":
        print("found")
        
    map_obj.insert(code, preReqs)
        




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

def print_prerequisites_from_map(course, level=0):
    indent = "  " * level
    prereqs = map_obj.get_prereqs(course)

    # Check if the prerequisites list is empty or contains 'None'
    if not prereqs or prereqs == [None]:
        print(f"{indent}No prerequisites for {course}")
        return
    
    print(f"{indent}Prerequisites for {course}: {prereqs}")

    # Iterate through the prerequisites
    for prereq in prereqs:
        # If the prerequisite is not 'None', recursively print its prerequisites
        if prereq is not None:
            print_prerequisites_from_map(prereq, level + 1)

start_time = time.time()
print_prerequisites("COP3530")
end_time = time.time()
tree_time = end_time - start_time

start_time = time.time()
print_prerequisites_from_map("COP3530")
end_time = time.time()
map_time = end_time - start_time

print(f"tree time: {tree_time} seconds")
print(f"map  time: {map_time} seconds")

print(map_obj.get_prereqs("MAC2311"))


"""
import json
import tree

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

tree_obj = tree.classTree()

for course in all_Courses:
    code = course.get('code')
    name = course.get('name')
    prerequisites = course.get('prerequisites')
    tree_obj.insert(code, prerequisites)

for course in all_Courses:
    code = course.get('code')
    vector = tree_obj.get_vector(code)
    print(vector)
    
tree_obj.insert("EEC6905", ['Prereq: ADV 3008 and MAR 3023 with minimum grades of C and Advertising major of junior standing or higher.'])  # Insert a class code with its corresponding vector
vector = tree_obj.get_vector("EEC6905")  # Retrieve the vector for a given class code
print(vector)

# joseph tst comment


count = 0

# for course in all_Courses:
#     print(count)
#     count += 1

#     code = course.get('code')
#     print(code)
#     #name = course.get('name')
#     # print(name)
#     # sections = course.get('sections')
#     # for section in sections:
#     #     classNumber = section.get('classNumber')
#     #     print(classNumber)

# print(count)
"""