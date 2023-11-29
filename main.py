import json
import tree
import re

with open('all_data.json', 'r') as f:
    all_Courses = json.load(f)

tree_obj = tree.classTree()

for course in all_Courses:

    code = course.get('code')
    name = course.get('name')
    prerequisites = course.get('prerequisites')
    #class_codes = re.findall(r'[A-Z]{3} \d{4}', prerequisites)
    # class_codes = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
    # class_codes = [code.replace(" ", "") for code in class_codes]

    class_count = len([code for code in class_codes if re.match(r'[A-Z]{3}\d{4}[A-Z]?', code)])
    if class_count > 1:
        class_codes = re.findall(r'[A-Z]{3} \d{4}[A-Z]?|,|and|or|\(|\)', prerequisites)
        class_codes = [code.replace(" ", "") if re.match(r'[A-Z]{3}\d{4}[A-Z]?', code) else code for code in class_codes]
    else:
        class_codes = re.findall(r'[A-Z]{3} \d{4}[A-Z]?', prerequisites)
        class_codes = [code.replace(" ", "") for code in class_codes]
        print(class_codes)

    
    print(class_codes)
    print(prerequisites)

    tree_obj.insert(code, prerequisites)






# for course in all_Courses:
#     code = course.get('code')
#     vector = tree_obj.get_vector(code)
#     print(vector)

# tree_obj.insert("EEC6905", ['Prereq: ADV 3008 and MAR 3023 with minimum grades of C and Advertising major of junior standing or higher.'])  # Insert a class code with its corresponding vector
# vector = tree_obj.get_vector("EEC6905")  # Retrieve the vector for a given class code
# print(vector)




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