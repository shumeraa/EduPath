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


    if "AP credit for" not in prerequisites:
        preReqs = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
        preReqs = [code.replace(" ", "") for code in preReqs]
    

    # if re.search(r'\b(AP|IBA)\b', prerequisites):

    tree_obj.insert(code, preReqs)
    # print(preReqs)
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

prereq_tree = Tree()

def add_prerequisites_to_tree(course, parent=None):
    prereqs = tree_obj.get_vector(course)
    
    # Add the course as a node to the tree. If it has a parent, specify it.
    if not prereq_tree.contains(course):
        prereq_tree.create_node(course, course, parent=parent)
    
    # If there are no prerequisites, return as there's nothing to add to the tree
    if not prereqs or prereqs == [None]:
        return
    
    # Iterate through the prerequisites and recursively add them to the tree
    for prereq in prereqs:
        if prereq is not None:
            # Recursively add the current prerequisite as a child of the course
            add_prerequisites_to_tree(prereq, course)





add_prerequisites_to_tree('COP3530')
prereq_tree.show()
# print(tree_obj.get_vector('COP3530'))
# print(tree_obj.get_vector('COT3100'))
# print(tree_obj.get_vector('MAC2234'))
# print(tree_obj.get_vector('MAC2312'))
# print(tree_obj.get_vector('MAC2512'))
# print(tree_obj.get_vector('MAC3473'))





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