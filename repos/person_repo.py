from validators.person_validator import *


class PersonRepository:
    def __init__(self):
        self.__person_list = []

    def add(self, person: Person):
        """
        Adauga o persoana in lista
        :param person:
        :return:
        """
        validate_person(person)
        if person.get_id() in self.__person_list:
            raise ValueError(f'Persoana cu id-ul {person.get_id()} se afla deja in lista')
        self.__person_list[person.get_id()] = person
