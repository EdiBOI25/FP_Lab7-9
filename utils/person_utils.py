from domain.person import Person
from validators.person_validator import *





def remove_person(person_list, person: Person):
    """
    Sterge o persoana din lista de persoane
    :param person_list:
    :param person:
    """
    if person not in person_list:
        raise ValueError(f'{person.get_name()} nu se afla in lista.')
    person_list.remove(person)


def search_person_by_id(person_list, idcode) -> Person:
    """
    Cauta o persoana dupa ID in lista de persoane si o returneaza
    :param person_list:
    :param idcode:
    :return:
    """
    for person in person_list:
        if person.get_id() == idcode:
            return person
    raise ValueError(f'Nu exista persoana cu id-ul {idcode} in lista')


def update_person(person: Person) -> Person:
    """
    Modifica datele unei persoane
    :param person:
    :return:
    """
    try:
        validate(person)
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
