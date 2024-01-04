import os
def NoOfStudents():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students > 0:
                return num_students
            else:
                print("Invalid number of students. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def NoOfCourses():
    while True:
        try:
            num_courses = int(input("Enter the number of courses: "))
            if num_courses > 0:
                return num_courses
            else:
                print("Invalid number of courses. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def GetInformation(student, students):
    print(f"---------INFORMATION OF STUDENT No {student+1}---------")
    student_id = input("     Enter student ID: ")
    name = input("     Enter student name: ")
    dob = input("     Enter student date of birth: ")
    students.append ({'id': student_id, 'name': name, 'dob': dob})


def GetCourseInformation(courseNo, courses):
    print(f"---------INFORMATION OF COURSE No {courseNo+1}---------")
    course_id = input("     Enter course ID: ")
    course_name = input("     Enter course name: ")
    courses.append({'id': course_id, 'name': course_name})

def student_mark(course, students):
    marks = {}
    print(f"Enter marks for students in course {course['name']}:")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} ({student['id']}): "))
        marks[student['id']] = mark
    return marks

def list_courses(courses):
    print("---------LIST OF COURSES---------")
    i = 0
    for course in courses:
        print(f"{i+1}.{course['id']}. {course['name']}")
        i=i+1

def list_students(students):
    print("---------LIST OF STUDENTS---------")
    i = 0
    for student in students:
        
        print(f"{i+1}.{student['id']}. {student['name']}")
        i=i+1

def show_student_marks(course, students, marks):
    print(f"---------STUDENT MARKS OF {course['name']} COURSE---------")
    for student in students:
        mark = marks.get(student['id'])
        print(f"{student['name']} ({student['id']}): {mark}")

def display_menu():
    print("---------MENU---------")
    print("1. List Courses")
    print("2. List Students")
    print("3. Show Student Marks for a Course")
    print("4. Add Student")
    print("5. Add Subject")
    print("6. Add Marks for a Student in a Course")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

# Input student information
students = []

# Input course information
courses = []

# Input and list student marks for each course


while True:
    user_choice = display_menu()
    
    if user_choice == '1':
        if courses == [] :
            os.system('cls')
            print("You haven't add any courses yet")
        else :
            list_courses(courses)
    elif user_choice == '2':
        if students == [] :
            os.system('cls')
            print("You haven't add any student yet")
        else :
            list_students(students)
    elif user_choice == '3':
        os.system('cls')
        course_choice = int(input("Enter the course number to show student marks: "))
        show_student_marks(courses[course_choice - 1], students)
    elif user_choice == '4':
        os.system('cls')
        num_students = NoOfStudents()
        new_student = [GetInformation(i, students) for i in range(num_students)]
        print("Student added successfully!")
    elif user_choice == '5':
        os.system('cls')
        num_courses = NoOfCourses()
        new_course = [GetCourseInformation(i, courses) for i in range(num_courses)]
        print("Subject added successfully!")
    elif user_choice == '6':
        os.system('cls')
        list_courses(courses)
        course_choice = int(input("Enter the course number to add marks for a student: "))
        list_students(students)
        student_choice = int(input("Enter the student number to add marks: "))
        mark = float(input(f"Enter marks for {students[student_choice - 1]['name']} "
                            f"({students[student_choice - 1]['id']}) in "
                            f"{courses[course_choice - 1]['name']}: "))
        courses[mark[students[student_choice - 1]['id']]] = mark
        print("Marks added successfully!")
    elif user_choice == '7':
        os.system('cls')
        print("Exiting program. Goodbye!")
        break
    else:
        os.system('cls')
        print("Invalid choice. Please enter a number between 1 and 7.")
