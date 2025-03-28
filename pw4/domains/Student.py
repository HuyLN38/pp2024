from domains.Entity import Entity

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
    
