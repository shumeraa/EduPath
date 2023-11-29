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





#IDS2935 Quest2 course
#The world and big data
#example2
for course in all_Courses:
    code = course.get('code')
    vector = tree_obj.get_vector(code)
    print(vector)

tree_obj.insert("EEC6905", ['Prereq: ADV 3008 and MAR 3023 with minimum grades of C and Advertising major of junior standing or higher.'])  # Insert a class code with its corresponding vector
vector = tree_obj.get_vector("EEC6905")  # Retrieve the vector for a given class code
print(vector)




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