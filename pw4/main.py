from domains import *

from output import display_menu
import os

# Main
school = SchoolSystem()
Student_list = Student()
Course_list = Course()

while True:
    print("\n")
    user_choice = display_menu()

    if user_choice == '1':
        os.system('cls')
        if school.courses == []:
            print("You haven't add any courses yet")
        else:
            school.list_courses()
    elif user_choice == '2':
        os.system('cls')
        if school.students == []:
            print("You haven't add any student yet")
        else:
            school.list_students()
    elif user_choice == '3':
        os.system('cls')
        if school.courses == []:
            print("You haven't add any courses yet")
        else :
            school.list_courses()
            while True:
                course_choice = int(input("Enter the course number to show marks for a student ( 0 to quit ) : "))
                if (course_choice < 0 or course_choice > len(school.courses)):
                    print("Wrong input")
                elif course_choice == 0 :
                    break
                else :
                    school.show_student_marks(school.courses[course_choice - 1])
                    break
    elif user_choice == '4':
        os.system('cls')
        new_students = Student_list.input()
        school.students.extend(new_students)
        print("Students added successfully!")
    elif user_choice == '5':
        os.system('cls')
        new_courses = Course_list.input(school.students)
        school.courses.extend(new_courses)
        print("Courses added successfully!")
    elif user_choice == '6':
        os.system('cls')
        school.list_courses()
        while True:
            course_choice = int(input("Enter the course number to add marks for a student ( 0 to quit ): "))
            if (course_choice < 0 or course_choice > len(school.courses)):
                print("Wrong input")
            elif course_choice == 0 :
                break
            else:
                break 
        school.list_students()
        while True :
            student_choice = int(input("Enter the student number to add marks ( 0 to quit ) : "))
            if (student_choice < 0 or student_choice > len(school.students)):
                print("Wrong input")
            elif course_choice == 0 :
                break
            else :
                mark = float(input(f"Enter marks for {school.students[student_choice - 1].get_name()} "
                            f"({school.students[student_choice - 1].get_id()}) in "
                            f"{school.courses[course_choice - 1].get_name()}: "))
                school.courses[course_choice - 1].set_marks(school.students[student_choice - 1].get_id(), mark)
                print("Marks added successfully!")
                break
    elif user_choice == '7':
        os.system('cls')
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
