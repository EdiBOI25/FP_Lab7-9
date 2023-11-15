from validators.person_validator import *
# TODO: aici si la event_repo, modifica chestiile astfel incat sa se modifice chestii in functie de id
#   de ex, la modify_person, sa nu mai transmiti persoana, ci ID-ul persoane pe care vrei sa o modifici
#   apoi refa testele corespunzatoare
#   ideea e sa nu poti modifica id-ul unei persoane/eveniment
# TODO 2: fa un "register" repo care sa contina o lista de perechi de genu (id_client, id_event) si sterge
#   lista de eventuri/persoane din clasele person/event


class PersonRepository:
    def __init__(self):
        self.__person_list = []
        self.__validator = PersonValidator()

    def __str__(self):
        string = ''
        for person in self.__person_list:
            string += str(person)
            string += '\n'
        return string

    def get_person_list(self):
        return self.__person_list

    def __getitem__(self, index):
        return self.__person_list[index]

    def is_id_in_list(self, idcode):
        for person in self.__person_list:
            if person.get_id() == idcode:
                return True
        return False

    def add_person(self, person: Person):
        """
        Adauga o persoana in lista
        :param person: Obiect de tip persoana
        """
        self.__validator.validate_person(person)
        if self.is_id_in_list(person.get_id()):
            raise ValueError(f'Persoana cu id-ul {person.get_id()} se afla deja in lista')
        self.__person_list.append(person)

    def remove_person(self, person: Person):
        """
        Sterge o persoana din lista de persoane
        :param person: Obiect de tip persoana
        """
        if person in self.__person_list:
            self.__person_list.remove(person)
            return
        raise ValueError(f'Persoana pe care vrei sa o stergi nu se afla in lista.')

    def search_person_by_id(self, idcode) -> Person:
        """
        Cauta o persoana dupa ID in lista de persoane si o returneaza
        :param idcode: ID-ul dupa care cautam persoana
        :return: persoana cautata
        """
        for person in self.__person_list:
            if person.get_id() == idcode:
                return person
        raise ValueError(f'Nu exista persoana cu id-ul {idcode} in lista')

    def update_person(self, id_code, new_name, new_address):
        """
        Modifica datele persoanei cu id-ul id_code
        :param id_code: id-ul persoanei careia vrem sa ii modificam datele
        :param new_name: numele nou
        :param new_address: adresa noua
        :return:
        """
        for person in self.__person_list:
            if id_code == person.get_id():
                new_person = Person(id_code, new_name, new_address)
                self.__validator.validate_person(new_person)
                index = self.__person_list.index(person)
                self.__person_list[index] = new_person
                return

        raise ValueError(f'Persoana cu id-ul {id_code} nu se afla in lista.')

