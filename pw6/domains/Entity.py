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