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
