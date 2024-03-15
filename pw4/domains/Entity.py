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