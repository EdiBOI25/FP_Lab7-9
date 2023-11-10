from repos.person_repo import PersonRepository
from domain.person import Person


def test_person_repo():
    person_list = PersonRepository()

    bob = Person(1234, 'Bob', 'Somesului 12')
    try:
        person_list.add_person(bob)
        assert True
    except ValueError:
        assert False
    try:
        person_list.add_person(Person('', 'Bob', 'AOsidj'))
        assert False
    except ValueError:
        assert True
    try:
        person_list.add_person(Person(1234, 'Bob', 'Somesului 12'))
        assert False
    except ValueError:
        assert True
