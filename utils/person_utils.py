from domain.person import Person


def add_person(person_list, person: Person):
    if person in person_list:
        print(f'{person.get_name()} se afla deja in lista.')
        return
    person_list.append(person)


def remove_person(person_list, person: Person):
    if person not in person_list:
        print(f'{person.get_name()} nu a fost gasit in lista.')
        return
    person_list.remove(person)


def search_person_by_id(person_list, idcode) -> Person:
    for person in person_list:
        if person.get_id() == idcode:
            return person
