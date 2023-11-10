from domain.person import Person
from validators.person_validator import *


def update_person(person: Person) -> Person:
    """
    Modifica datele unei persoane
    :param person:
    :return:
    """
    try:
        validate_person(person)
        return person
    except ValueError:
        pass


def update_person_name(person: Person, name):
    pass


def generate_id(person_list):
    """
    Genereaza un ID nou
    :param person_list: lista de persoane
    :return:
    """
    result_id = 0
    for person in person_list:
        result_id = max(result_id, person.get_id())
    return result_id + 1
