from repos.person_repo import *
from utils import general_utils


class PersonService:
    def __init__(self):
        self.__repo = PersonRepository()

    def get_all(self):
        return self.__repo.get_all()

    def __str__(self):
        return str(self.__repo)

    def add_person(self, name, address):
        idcode = general_utils.generate_id(self.__repo.get_all())
        self.__repo.add_person(Person(idcode, name, address))

    def remove_person(self, idcode):
        person = self.search_by_id(idcode)
        self.__repo.remove_person(person)

    def search_by_id(self, idcode):
        return self.__repo.search_person_by_id(idcode)

    def update_person(self, idcode, new_name, new_address):
        self.__repo.update_person(idcode, new_name, new_address)
