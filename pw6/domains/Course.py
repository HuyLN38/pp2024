from domains.Entity import Entity
import pickle
                                                             
#  ██████╗ ██████╗ ██╗   ██╗██████╗ ███████╗███████╗
# ██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝
# ██║     ██║   ██║██║   ██║██████╔╝███████╗█████╗  
# ██║     ██║   ██║██║   ██║██╔══██╗╚════██║██╔══╝  
# ╚██████╗╚██████╔╝╚██████╔╝██║  ██║███████║███████╗
#  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝
                                                  
class Course(Entity):
    def __init__(self):
        super().__init__()
        self.__marks = {}
    
    def get_marks(self):
        return self.__marks

    def set_marks(self, student_id, mark):
        self.__marks[student_id] = mark

    def input(self):
        courses = []
        course_count = self.check_and_get_positive("Enter the number of courses: ")
        for i in range(course_count):
            course_id = input(f"Enter course ID for course {i+1}: ")
            name = input(f"Enter course name for course {i+1}: ")
            course = Course()
            course.set_id(course_id)
            course.set_name(name)
            courses.append(course)
        
        # Write course info to courses.txt
        with open("courses.txt", "w") as file:
            for course in courses:
                file.write(f"Course ID: {course.get_id()}, Course Name: {course.get_name()}\n")
            file.close()
        with open("courses.txt", 'wb') as f:
            pickle.dump("courses.txt", f)
        return courses

