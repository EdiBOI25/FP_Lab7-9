from utils.general_utils import *
from domain.event import Event
from domain.person import Person
import datetime


def test_generate_id():
    random_list = [1,2,'lol', Person(1, 'ed', 'brasov')]
    try:
        new_id = generate_id(random_list)
        assert False
    except TypeError as e:
        assert str(e) == 'Cel putin un element in lista nu este de tipul Persoana sau Eveniment.'
    random_list2 = [Person(1, 'bob', 'brasov'), Event(
        2, datetime.date(2020, 1, 2),
        datetime.time(2, 30),
        'random description'
    )]
    try:
        new_id = generate_id(random_list2)
        assert new_id == 3
    except ValueError:
        assert False
