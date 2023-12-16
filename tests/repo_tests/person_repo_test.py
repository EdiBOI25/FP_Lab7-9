from repos.person_repo import *


def test_person_repo():
    person_file = 'tests/repo_tests/people.txt'
    try:
        PersonFileRepository('text.txt').load_from_file()
        assert False
    except FileNotFoundError as e:
        assert str(e) == '[Errno 2] No such file or directory: \'text.txt\''
    open(person_file, 'w').close()
    assert PersonFileRepository(person_file).load_from_file() == []
    lst = [
        Person(1234, 'Bob', 'Somesului 12'),
        Person(2525, 'nanami', 'japan')
    ]
    PersonFileRepository(person_file).store_to_file(lst)
    assert PersonFileRepository(person_file).load_from_file() == [
        Person(1234, 'Bob', 'Somesului 12'),
        Person(2525, 'nanami', 'japan')
    ]

    open(person_file, 'w').close()
    person_list = PersonRepository(person_file)

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
