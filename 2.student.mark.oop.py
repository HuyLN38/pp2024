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
            course.input_marks(students)
            courses.append(course)
        return courses   
    
    def input_marks(self, students):
        for student in students:
            mark = float(input(f"Enter marks for {student.get_name()} ({student.get_id()}): "))
            self.set_marks(student.get_id(), mark)    

class SchoolSystem(Entity):
    def __init__(self):
        self.students = []
        self.courses = []

    def list_courses(self):
        print("---------LIST OF COURSES---------")
        for course in self.courses:
            course.list()

    def list_students(self):
        print("---------LIST OF STUDENTS---------")
        for student in self.students:
            student.list()

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

# Main
school = SchoolSystem()
Student_list = Student()
Course_list = Course()
school.students = Student_list.input()
school.courses = Course_list.input(school.students)
print("\n\n\n\n")
school.list_courses()
school.list_students()
for course in school.courses:
    school.show_student_marks(course)
