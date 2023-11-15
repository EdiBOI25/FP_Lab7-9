from service.person_service import *


def test_person_service():
    person_service = PersonService()
    assert person_service.get_all() == []
    try:
        person_service.add_person('Bob', 'Pitesti')
        assert person_service.get_all()[0] == Person(1, 'Bob', 'Pitesti')
    except ValueError as e:
        assert False
    try:
        person_service.add_person('', '')
        assert False
    except ValueError as e:
        assert str(e) == 'Numele nu poate fi gol, Adresa nu poate fi goala'
    try:
        person_service.add_person('Bob2', 'Brasov')
        assert person_service.get_all()[1] == Person(2, 'Bob2', 'Brasov')
        assert len(person_service.get_all()) == 2
    except ValueError:
        assert False
