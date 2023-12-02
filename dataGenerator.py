import json
import random
import string
import main

def generate_course_code():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    numbers = ''.join(random.choices(string.digits, k=4))
    return letters + numbers

def generate_prerequisites(num_prereqs=3):
    prerequisites = []
    for i in range(num_prereqs):
        prerequisites.append(generate_course_code())
    return prerequisites

def create_additional_courses(num_courses=90000):
    new_courses = []
    for j in range(num_courses):
        course_code = generate_course_code()
        prereqs = generate_prerequisites(random.randint(0, 5)) 
        new_courses.append({"code": course_code, "prerequisites": prereqs})
    return new_courses

def create_additional_courses_up_to_limit(num_courses=90000, limit=100000):
    with open('all_data.json', 'r') as file:
        existing_courses = json.load(file)

    current_course_count = len(existing_courses)
    if current_course_count >= limit:
        print(f"The dataset already has {current_course_count} courses.")
        return existing_courses

    courses_to_add = limit - current_course_count
    print(f"Adding {courses_to_add} courses to reach the limit of {limit}.")

    new_courses = create_additional_courses(courses_to_add)

    all_courses = existing_courses + new_courses

    with open('all_data.json', 'w') as file:
        json.dump(all_courses, file, indent=4)

    return all_courses

def modify_dataset(filename='all_data.json', desired_count=100000):
    # Load the dataset
    with open(filename, 'r') as file:
        courses = json.load(file)

    # Trim the dataset if it's larger than desired_count
    courses = courses[:desired_count]

    # Ensure each course has 0 to 3 prerequisites
    for course in courses:
        prereq_count = random.randint(0, 3)  # Randomly choose number of prerequisites (0 to 3)
        course['prerequisites'] = random.sample(course['prerequisites'], min(prereq_count, len(course['prerequisites'])))
        
        # If there are not enough prerequisites, generate additional ones
        if len(course['prerequisites']) < prereq_count:
            course['prerequisites'].extend(main.generate_random_courses(prereq_count - len(course['prerequisites'])))

    # Save the modified dataset
    with open(filename, 'w') as file:
        json.dump(courses, file, indent=4)

    return courses

all_courses = create_additional_courses_up_to_limit()

all_courses = modify_dataset()

print(f"Total courses in the updated dataset: {len(all_courses)}")
