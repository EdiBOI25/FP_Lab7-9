from domain.person import Person


def validate_person(person: Person):
    if person.get_id() == '':
        raise ValueError('Person ID cannot be empty')
    if person.get_name() == '':
        raise ValueError('Person name cannot be empty')
    if person.get_address() == '':
        raise ValueError('Person address cannot be empty')

