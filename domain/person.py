class Person:
    def __init__(self, person_id: int, name: str, address: str):
        """
        Creeaza o noua persoana
        """
        self.__id = person_id
        self.__name = name
        self.__address = address

    def __eq__(self, other):
        """
        Defineste egalitatea dintre doua persoane
        :return: True/False
        """
        if not isinstance(other, Person):
            return False
        return self.__id == other.get_id()

    def __str__(self):
        """
        :return: Reprezentarea unei Persoane in string
        """
        return f'Person(ID: {self.__id}, Nume: {self.__name}, Adresa: {self.__address})'

    # Getters and Setters
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_id(self, new_id: int):
        self.__id = new_id

    def set_name(self, new_name: str):
        self.__name = new_name

    def set_address(self, new_address: str):
        self.__address = new_address
