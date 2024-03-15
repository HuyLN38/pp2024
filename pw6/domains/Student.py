from domains.Entity import Entity
import pickle

# ███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗
# ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
# ███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   
# ╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   
# ███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   
# ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   

class Student(Entity):
    def __init__(self):
        super().__init__()
        self.__dob = None

    def set_dob(self, dob):
        self.__dob = dob

    def get_dob(self):
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
        
        with open("students.txt", "w") as file:
            for student in temp:
                file.write(f"Student ID: {student.get_id()}\n")
                file.write(f"Name: {student.get_name()}\n")
                file.write(f"Date of Birth: {student.get_dob()}\n")
                file.write("\n")
            file.close()

        with open("students.txt", 'wb') as f:
            pickle.dump("students.txt", f)
        return temp
        
