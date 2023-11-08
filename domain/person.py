class Person:
    attendance_list = []

    def __init__(self, person_id: str, name: str, address: str):
        self.__id = person_id
        self.__name = name
        self.__address = address

    # Getters and Setters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_id(self, new_id):
        self.__id = new_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address
