import string

from repos.person_repo import *
from utils import general_utils
import random


class PersonService:
    def __init__(self, per_f):
        self.__repo = PersonRepository(per_f)

    def get_all(self):
        return self.__repo.get_all()

    def __str__(self):
        return str(self.__repo)

    def add_person(self, name, address):
        """
        Adauga persoana
        :param name:
        :param address:
        :return:
        """
        idcode = general_utils.generate_id(self.__repo.get_all())
        self.__repo.add_person(Person(idcode, name, address))

    def remove_person(self, idcode):
        """
        Sterge persoana
        :param idcode:
        :return:
        """
        person = self.search_by_id(idcode)
        self.__repo.remove_person(person)

    def search_by_id(self, idcode):
        """
        Cauta persoana prin id
        :param idcode:
        :return: persoana cautata
        """
        return self.__repo.search_person_by_id(idcode)

    def update_person(self, idcode, new_name, new_address):
        """
        Modifica datele unei persoane
        :param idcode:
        :param new_name:
        :param new_address:
        :return:
        """
        self.__repo.update_person(idcode, new_name, new_address)

    @staticmethod
    def __random_name(max_length):
        """
        Generates random name
        :param max_length: Maximum length of name
        :return:
        """
        name = ''
        name += random.choice(string.ascii_uppercase)
        for i in range(max_length - 1):
            name += random.choice(string.ascii_lowercase)
        return name

    def __random_address(self, max_length):
        """
        Generates random address
        :param max_length: Maximum length of address
        :return:
        """
        address = self.__random_name(max_length)
        address += ' '
        address += str(random.randint(1, 100))
        return address

    def add_random_people(self, limit):
        """
        Adds a random number of people with random names and addresses
        :param limit: The max number of people to add
        :return:
        """
        num = random.randint(1, limit)
        for i in range(1, num+1):
            name = self.__random_name(20)
            address = self.__random_address(50)
            self.add_person(name, address)
