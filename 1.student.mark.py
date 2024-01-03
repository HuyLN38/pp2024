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

def GetInformation(student):
    print(f"---------INFORMATION OF STUDENT No {student+1}---------")
    student_id = input("     Enter student ID: ")
    name = input("     Enter student name: ")
    dob = input("     Enter student date of birth: ")
    return {'id': student_id, 'name': name, 'dob': dob}


def GetCourseInformation(courseNo):
    print(f"---------INFORMATION OF COURSE No {courseNo+1}---------")
    course_id = input("     Enter course ID: ")
    course_name = input("     Enter course name: ")
    return {'id': course_id, 'name': course_name}

def student_mark(course, students):
    marks = {}
    print(f"Enter marks for students in course {course['name']}:")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} ({student['id']}): "))
        marks[student['id']] = mark
    return marks

def list_courses(courses):
    print("---------LIST OF COURSES---------")
    for course in courses:
        print(f"{course['id']}. {course['name']}")

def list_students(students):
    print("---------LIST OF STUDENTS---------")
    for student in students:
        print(f"{student['id']}. {student['name']}")

def show_student_marks(course, students, marks):
    print(f"---------STUDENT MARKS OF {course['name']} COURSE---------")
    for student in students:
        mark = marks.get(student['id'])
        print(f"{student['name']} ({student['id']}): {mark}")

# Input number of students
num_students = NoOfStudents()

# Input student information
students =  [GetInformation(i) for i in range(num_students)]

# Input number of courses
num_courses = NoOfCourses()

# Input course information
courses = [GetCourseInformation(i) for i in range(num_courses)]

# Input and list student marks for each course
for course in courses:
    marks = student_mark(course, students)
list_courses(courses)
list_students(students)
for i in (courses):
    show_student_marks(i, students, marks)

