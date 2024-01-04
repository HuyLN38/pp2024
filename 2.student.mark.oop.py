import os
class Entity:
    def __init__(self):
        self.__id = None
        self.__name = None

    def set_id(self, id):
        self.__id = id
    
    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def list(self):
        print(f"{self.get_id()}. {self.get_name()}")

    def input(self):
        entity_count = self.check_and_get_positive("Enter the number of Entity: ")
        entities = []
        for i in range(entity_count):
            entity_id = input(f"Enter ID for Entity {i+1}: ")
            name = input(f"Enter name for Entity {i+1}: ")
            entity = Entity()
            entity.set_id(entity_id)
            entity.set_name(name)
            entities.append(entity)    
        return entities
    
    def check_and_get_positive(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                else:
                    print("Invalid input. Please enter a positive integer.")
            except ValueError:
                print("Invalid input. Please enter an integer.")    


class Student(Entity):
    def __init__(self):
        super().__init__()
        self.__dob = None

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(dob):
        return self.__dob
    
    def input(self):
        temp = []
        student_count = self.check_and_get_positive("Enter the number of students: ")
        for i in range(student_count):
            student_id = input(f"Enter student ID for student {i+1}: ")
            name = input(f"Enter student name for student {i+1}: ")
            dob = input(f"Enter student date of birth for student {i+1}: ")
            student = Student()
            student.set_id(student_id)
            student.set_name(name)
            student.set_dob(dob)
            temp.append(student)    
        return temp

class Course(Entity):
    def __init__(self):
        super().__init__()
        self.__marks = {}
    
    def get_marks(self):
        return self.__marks

    def set_marks(self, student_id, mark):
        self.__marks[student_id] = mark

    def input(self, students):
        courses=[]
        course_count = self.check_and_get_positive("Enter the number of courses: ")
        for i in range(course_count):
            course_id = input(f"Enter course ID for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            course = Course()
            course.set_id(course_id)
            course.set_name(name)
            courses.append(course)
        return courses      

class SchoolSystem(Entity):
    def __init__(self):
        self.students = []
        self.courses = []

    def list_courses(self):
        print("---------LIST OF COURSES---------")
        i = 0
        for course in self.courses:
            print(f"{i+1}.", end =" ")
            course.list()
            i = i+1

    def list_students(self):
        print("---------LIST OF STUDENTS---------")
        i = 0
        for student in self.students:
            print(f"{i+1}.", end =" ")
            student.list()
            i = i+1

    def show_student_marks(self, course):
        print(f"---------STUDENT MARKS OF {course.get_name()} COURSE---------")
        for student_id, mark in course.get_marks().items():
            student = self.student_by_id(student_id)
            print(f"{student.get_name()} ({student.get_id()}): {mark}")

    def student_by_id(self, student_id):
        for student in self.students:
            if student.get_id() == student_id:
                return student
        return None

def display_menu():
    print("---------MENU---------")
    print("1. List Courses")
    print("2. List Students")
    print("3. Show Student Marks for a Course")
    print("4. Add Student")
    print("5. Add Course")
    print("6. Add Marks for a Student in a Course")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    return choice

# Main
school = SchoolSystem()
Student_list = Student()
Course_list = Course()

while True:
    user_choice = display_menu()

    if user_choice == '1':
        os.system('cls')
        if school.courses == []:
            print("You haven't add any courses yet")
        school.list_courses()
    elif user_choice == '2':
        os.system('cls')
        if school.students == []:
            print("You haven't add any student yet")
        school.list_students()
    elif user_choice == '3':
        os.system('cls')
        school.list_courses()
        course_choice = int(input("Enter the course number to show student marks: "))
        school.show_student_marks(school.courses[course_choice - 1])
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
        course_choice = int(input("Enter the course number to add marks for a student: "))
        school.list_students()
        student_choice = int(input("Enter the student number to add marks: "))
        mark = float(input(f"Enter marks for {school.students[student_choice - 1].get_name()} "
                            f"({school.students[student_choice - 1].get_id()}) in "
                            f"{school.courses[course_choice - 1].get_name()}: "))
        school.courses[course_choice - 1].set_marks(school.students[student_choice - 1].get_id(), mark)
        print("Marks added successfully!")
    elif user_choice == '7':
        os.system('cls')
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
