import json
import tree
import re
from treelib import Node, Tree

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

tree_obj = tree.classTree()

for course in all_Courses:
    code = course.get('code')
    name = course.get('name')
    prerequisites = course.get('prerequisites')
    preReqs = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
    preReqs = [code.replace(" ", "") for code in preReqs]
    tree_obj.insert(code, preReqs)
    # print(class_codes)
    # print(prerequisites)



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

print_prerequisites('COP3530')





# for course in all_Courses:
#     code = course.get('code')
#     vector = tree_obj.get_vector(code)
#     print(vector)





# count = 0

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