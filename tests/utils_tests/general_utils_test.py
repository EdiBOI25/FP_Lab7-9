from utils.general_utils import *
from domain.event import Event
from domain.person import Person
import datetime


def test_generate_id():
    random_list = [1, 2, 'lol', Person(1, 'ed', 'brasov')]
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


def test_sort_event_list_by_description():
    new_list = [
        Event(1, datetime.date(2020, 2, 2), datetime.time(2, 20), 'asdf'),
        Event(2, datetime.date(2025, 2, 2), datetime.time(2, 20), 'absdf'),
        Event(3, datetime.date(2010, 2, 2), datetime.time(2, 20), 'jsdf'),
        Event(4, datetime.date(2020, 3, 2), datetime.time(2, 20), 'zsdf'),
        Event(5, datetime.date(2020, 1, 2), datetime.time(2, 20), 'aasdf')
    ]
    result = sort_event_list_by_description(new_list)
    result = list(map(lambda ident: ident.get_id(), result))
    assert result == [5, 2, 1, 3, 4]
    result2 = sort_event_list_by_date(new_list)
    result2 = list(map(lambda ident: ident.get_id(), result2))
    assert result2 == [3, 5, 1, 4, 2]
    try:
        sort_event_list_by_description([1, 2, 3])
        assert False
    except TypeError as e:
        assert str(e) == 'Cel putin un element in lista nu este de tipul Eveniment.'


def test_bubble_sort():
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4], reverse=True) == [4, 3, 2, 1]
    fructe = {'mere': 30, 'pere': 20, 'afine': 10}
    assert bubble_sort(fructe, key=lambda x: fructe[x]) == ['afine', 'pere', 'mere']
    assert bubble_sort(fructe, key=lambda x: fructe[x], reverse=True) == ['mere', 'pere', 'afine']
    fructe = {'mere': 10, 'pere': 20, 'afine': 30}
    assert bubble_sort(fructe, key=lambda x: fructe[x], reverse=True) == ['afine', 'pere', 'mere']
    assert bubble_sort(['zz', 'aa', 'ce'], reverse=True) == ['zz', 'ce', 'aa']
    assert bubble_sort([4, 3, 2, 1], cmp=lambda x, y: x < y) == [1, 2, 3, 4]
    assert bubble_sort([1, 2, 3, 4], cmp=lambda x, y: x > y) == [4, 3, 2, 1]


def test_shell_sort():
    assert shell_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert shell_sort([1, 2, 3, 4], reverse=True) == [4, 3, 2, 1]
    fructe = {'mere': 30, 'pere': 20, 'afine': 10}
    assert shell_sort(fructe, key=lambda x: fructe[x]) == ['afine', 'pere', 'mere']
    assert shell_sort(fructe, key=lambda x: fructe[x], reverse=True) == ['mere', 'pere', 'afine']
    fructe = {'mere': 10, 'pere': 20, 'afine': 30}
    assert shell_sort(fructe, key=lambda x: fructe[x], reverse=True) == ['afine', 'pere', 'mere']
    assert shell_sort(['zz', 'aa', 'ce'], reverse=True) == ['zz', 'ce', 'aa']
    assert shell_sort([4, 3, 2, 1], cmp=lambda x, y: x < y) == [1, 2, 3, 4]
    assert shell_sort([1, 2, 3, 4], cmp=lambda x, y: x > y) == [4, 3, 2, 1]
