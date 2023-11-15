from repos.person_repo import *


def test_person_repo():
    person_list = PersonRepository()

    bob = Person(1234, 'Bob', 'Somesului 12')
    # add_person test
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

    # remove_person test
    nanami = Person(2525, 'nanami', 'japan')
    person_list.add_person(nanami)
    jogo = Person(1236, 'jogo', 'korea')
    person_list.add_person(jogo)
    try:
        person_list.remove_person(nanami)
        assert True
    except ValueError:
        assert False
    try:
        person_list.remove_person(Person(2525, 'gojo', 'china'))
        assert False
    except ValueError:
        assert True

    # search_person_by_id test
    try:
        result = person_list.search_person_by_id(1236)
        assert True
    except ValueError:
        assert False
    try:
        result = person_list.search_person_by_id(6541)
        assert False
    except ValueError:
        assert True

    # update_person test
    person_list.add_person(nanami)
    try:
        person_list.update_person(2525, 'nanami', 'tokyo')
        assert True
    except ValueError:
        assert False
    try:
        person_list.update_person(976, 'hatz', 'hatz2')
        assert False
    except ValueError:
        assert True
    try:
        person_list.update_person(2525, '', '')
        assert False
    except ValueError as e:
        assert str(e) == 'Numele nu poate fi gol, Adresa nu poate fi goala'
