import os
from domains.Entity import Entity
# ███████╗ ██████╗██╗  ██╗ ██████╗  ██████╗ ██╗         ███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗
# ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔═══██╗██║         ██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║
# ███████╗██║     ███████║██║   ██║██║   ██║██║         ███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║
# ╚════██║██║     ██╔══██║██║   ██║██║   ██║██║         ╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║
# ███████║╚██████╗██║  ██║╚██████╔╝╚██████╔╝███████╗    ███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║
# ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝

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
        if course.get_marks() == {}:
            os.system('cls')
            print("No mark added yet :(")
            return
        print(f"---------STUDENT MARKS OF {course.get_name()} COURSE---------")
        for student_id, mark in course.get_marks().items():
            student = self.student_by_id(student_id)
            print(f"{student.get_name()} ({student.get_id()}): {mark}")

    def student_by_id(self, student_id):
        for student in self.students:
            if student.get_id() == student_id:
                return student
        return None


