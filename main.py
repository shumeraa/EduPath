import json
import tree
import re
import map
import time
import getData
import os
import random



def main():
    tree_obj = tree.classTree()
    map_obj = map.HashMap()
    
    print("Populating Data... This may take a while (~30 seconds))")
    getData.populateUfData(tree_obj, map_obj)
    getData.populateRandomData(tree_obj, map_obj)
    print()

    firstRun = True
    while True:
        if(firstRun):
            print("\nWelcome to EduPath: Your Guide for Courses!")
            firstRun = False
        print()
        print("1. Display a Random Course's Prerequisite Graph")
        print("2. Display Prerequisite Graph for a UF Course")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            randomCourse = getData.getRandomClass()
            print(f"Randomly selected course: {randomCourse}")
            map_obj.getTimeAndGraph(randomCourse)
            tree_obj.getTimeAndGraph(randomCourse)

        elif choice == '2':
            course_code = input("Enter the course code: ").strip()
            course_code = course_code.upper()
            if(tree_obj.get_prereqs(course_code) == None or map_obj.get_prereqs(course_code) == None):
                print("Course not found")
                continue
            map_obj.getTimeAndGraph(course_code)
            tree_obj.getTimeAndGraph(course_code)
        elif choice == '3':
            print("Exiting EduPath. Goodbye!")
            break
        else:
            print()
            print("Invalid choice, please try again.")

main()








