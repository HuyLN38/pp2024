from domains.Entity import Entity
                                                             
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
