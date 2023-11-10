from domain.person import Person


def validate(person: Person):
    """
    Valideaza datele unei persoane
    :param person: persoana
    Exceptions: daca datele sunt goale
    """
    errors = ''
    if person.get_id() == '':
        errors += 'ID-ul nu poate fi gol'
    if person.get_name() == '':
        errors += 'Numele nu poate fi gol'
    if person.get_address() == '':
        errors += 'Adresa nu poate fi goala'
    if len(errors) > 0:
        raise ValueError(errors)
