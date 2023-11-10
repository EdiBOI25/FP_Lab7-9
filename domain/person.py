class Person:
    def __init__(self, person_id: int, name: str, address: str):
        self.__id = person_id
        self.__name = name
        self.__address = address
        self.__attendance_list = []

    # Getters and Setters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_attendance_list(self):
        return self.__attendance_list

    def set_id(self, new_id: int):
        self.__id = new_id

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_address(self, new_address: str):
        self.__address = new_address

    def set_attendance_list(self, new_list):
        self.__attendance_list = new_list

    def add_attending_event(self, event):
        self.__attendance_list.append(event)

    def remove_attending_event(self, event):
        self.__attendance_list.remove(event)
