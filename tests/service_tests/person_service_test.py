from service.person_service import *


def test_person_service():
    person_service = PersonService()
    # add_person
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
    assert person_service.search_by_id(2) == Person(2, 'Bob2', 'Brasov')

    # update person
    try:
        person_service.update_person(3, 'Emanuel2', 'Brasov, Coresi')
        assert False
    except ValueError as e:
        assert str(e) == 'Persoana cu id-ul 3 nu se afla in lista.'
    try:
        person_service.update_person(2, '', 'Brasov, Coresi')
        assert False
    except ValueError as e:
        assert str(e) == 'Numele nu poate fi gol'
    try:
        person_service.update_person(2, 'Emanuel2', 'Brasov, Coresi')
        assert person_service.search_by_id(2) == Person(2, 'Emanuel2', 'Brasov, Coresi')
    except ValueError:
        assert False

    # remove_person
    try:
        person_service.remove_person(3)
        assert False
    except ValueError as e:
        assert str(e) == 'Nu exista persoana cu id-ul 3 in lista'
    try:
        person_service.remove_person(2)
        assert len(person_service.get_all()) == 1
    except ValueError:
        assert False

    # add_random_persons
    random.seed(25)
    person_service.add_random_persons(20)
    assert len(person_service.get_all()) == 14
    assert person_service.search_by_id(10).get_name() == 'Jihmvayzkfibtsmgktza'
    random.seed(100)
    person_service.add_random_persons(20)
    assert person_service.search_by_id(15).get_address() == 'Ugkhjygfegllungmorizmfuudfatmeysfgfavhozumetrybthw 80'
    assert len(person_service.get_all()) == 19
