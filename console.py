# import tree
# import getData
import main

all_Courses, tree_obj = main.load_and_build_tree()

print("\nWelcome to EduPath: Your Guide for Courses!")
print("1. Print a Random Prerequisite Tree")
print("2. Display Course Prerequisites")
print("3. Exit")

choice = input("Enter your choice: ").strip()
1
if choice == '1':
     main.print_random_prerequisite_tree(all_Courses, tree_obj)
# elif choice == '2':
   
# elif choice == '3':
    
# elif choice == '4':
#     print("Exiting EduPath. Have a great day!")
# else:
#     print("Invalid choice. Please try again.")

