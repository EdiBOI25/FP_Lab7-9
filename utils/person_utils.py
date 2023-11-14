from domain.person import Person
from validators.person_validator import *


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
