# import tree
# import getData
import main

all_Courses, tree_obj = main.load_and_build_tree()

while True:
     print("\nWelcome to EduPath: Your Guide for Courses!")
     print("1. Print a Random Course and its Prerequisite")
     print("2. Display Course Prerequisites")
     print("3. Exit")

     choice = input("Enter your choice: ").strip()
     if choice == '1':
          main.print_random_prerequisite_tree(all_Courses, tree_obj)
     elif choice == '2':
          course_code = input("Enter the course code: ").strip()
          prerequisites = main.get_prerequisites(course_code, tree_obj)
          if prerequisites:
               print(f"{prerequisites}")
          else:
               print(f"No Prerequisities found for {course_code}.")
     elif choice == '3':
          print("Exiting EduPath. Goodbye!")
          break
     else:
          print("Invalid choice, please try again.")
