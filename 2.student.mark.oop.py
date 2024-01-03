class Student:
    def __init__(self, student_id, name, dob):
        self.id = student_id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, course_id, name):
        self.id = course_id
        self.name = name
        self.marks = {}

    def get_marks(self, students):
        for student in students:
            mark = float(input(f"Enter marks for {student.name} ({student.id}): "))
            self.marks[student.id] = mark

class SchoolSystem:
    
    def __init__(self):
        self.students = []
        self.courses = []

    def GetStudentInformation(self):
        student_count = self.CheckAndGetPositive("Enter the number of students: ")
        for i in range(student_count):
            student_id = input(f"Enter student ID for student {i+1}: ")
            name = input(f"Enter student name for student {i+1}: ")
            dob = input(f"Enter student date of birth for student {i+1}: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def GetCourseInformation(self):
        course_count = self.CheckAndGetPositive("Enter the number of courses: ")
        for i in range(course_count):
            course_id = input(f"Enter course ID for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            course = Course(course_id, name)
            self.courses.append(course)
            course.get_marks(self.students)

    def CheckAndGetPositive(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")

    def list_courses(self):
        print("---------LIST OF COURSES---------")
        for course in self.courses:
            print(f"{course.id}. {course.name}")

    def list_students(self):
        print("---------LIST OF STUDENTS---------")
        for student in self.students:
            print(f"{student.id}. {student.name}")

    def show_student_marks(self, course):
        print(f"---------STUDENT MARKS OF {course.name} COURSE---------")
        for student_id, mark in course.marks.items():
            student = self.student_by_id(student_id)
            print(f"{student.name} ({student.id}): {mark}")

    def student_by_id(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

# Main
school = SchoolSystem()
school.GetStudentInformation()
school.GetCourseInformation()
print("\n\n\n\n")
school.list_courses()
school.list_students()
for course in school.courses:
    school.show_student_marks(course)
