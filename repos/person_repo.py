from validators.person_validator import *


# TODO: test person_repo
#   event_repo + test_event_repo

class PersonRepository:
    def __init__(self):
        self.__person_list = []

    def get_person_list(self):
        return self.__person_list

    def __getitem__(self, index):
        return self.__person_list[index]

    def add_person(self, person: Person):
        """
        Adauga o persoana in lista
        :param person:
        """
        validate_person(person)
        for pers in self.__person_list:
            if person.get_id() == pers.get_id():
                raise ValueError(f'Persoana cu id-ul {person.get_id()} se afla deja in lista')
        self.__person_list.append(person)

    def remove_person(self, person: Person):
        """
        Sterge o persoana din lista de persoane
        :param person:
        """
        if person in self.__person_list:
            self.__person_list.remove(person)
        raise ValueError(f'Persoana pe care vrei sa o stergi nu se afla in lista.')

    def search_person_by_id(self, idcode) -> Person:
        """
        Cauta o persoana dupa ID in lista de persoane si o returneaza
        :param idcode:
        :return: persoana cautata
        """
        for person in self.__person_list:
            if person.get_id() == idcode:
                return person
        raise ValueError(f'Nu exista persoana cu id-ul {idcode} in lista')

    def update_person(self, person: Person, new_person: Person):
        """
        Modifica datele unei persoane
        :param new_person: Obiect persoana cu datele modificate
        :param person: Persoana carei vrem sa ii modificam datele
        :return:
        """
        validate_person(new_person)
        if person not in self.__person_list:
            raise ValueError(f'Persoana careia vrei sa ii modifici datele nu se afla in lista.')
        index = self.__person_list.index(person)
        self.__person_list[index] = new_person

    def update_person_id(self, person: Person, new_id):
        self.update_person(person, Person(new_id, person.get_name(), person.get_address()))

    def update_person_name(self, person: Person, new_name):
        self.update_person(person, Person(person.get_id(), new_name, person.get_address()))

    def update_person_address(self, person: Person, new_address):
        self.update_person(person, Person(person.get_id(), person.get_name(), new_address))
