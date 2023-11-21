from service.event_service import *
from datetime import date, time


def test_event_service():
    event_service = EventService()
    assert event_service.get_all() == []
    # add_event
    try:
        event_service.add_event(date(2020, 2, 4), time(1, 20), 'Random description')
        assert event_service.get_all()[0] == Event(1, date(2020, 2, 4), time(1, 20), 'Random description')
    except ValueError:
        assert False
    try:
        event_service.add_event('', '', '')
        assert False
    except ValueError as e:
        assert str(e) == 'Data nu poate fi goala, Durata nu poate fi goala, Descrierea nu poate fi goala'
    try:
        event_service.add_event(date(2023, 1, 25), time(5, 30), 'Birthday')
        assert event_service.get_all()[1] == Event(2, date(2023, 1, 25), time(5, 30), 'Birthday')
        assert len(event_service.get_all()) == 2
    except ValueError:
        assert False
    assert event_service.search_by_id(2) == Event(2, date(2023, 1, 25), time(5, 30), 'Birthday')

    # update_event
    try:
        event_service.update_event(3, date(1999, 1, 25), time(5, 30), 'Birthday')
        assert False
    except ValueError as e:
        assert str(e) == 'Evenimentul cu id-ul 3 nu se afla in lista.'
    try:
        event_service.update_event(2, '', time(5, 30), 'Birthday')
        assert False
    except ValueError as e:
        assert str(e) == 'Data nu poate fi goala'
    try:
        event_service.update_event(2, date(1999, 1, 25), time(5, 30), 'Birthday')
        assert event_service.search_by_id(2) == Event(2, date(1999, 1, 25), time(5, 30), 'Birthday')
    except ValueError:
        assert False

    # remove_event
    try:
        event_service.remove_event(3)
        assert False
    except ValueError as e:
        assert str(e) == 'Nu exista evenimentul cu id-ul 3 in lista'
    try:
        event_service.remove_event(2)
        assert len(event_service.get_all()) == 1
    except ValueError:
        assert False

    # random_events
    random.seed(25)
    event_service.add_random_events(20)
    assert event_service.search_by_id(5).get_date() == date(2018, 10, 26)
    assert len(event_service.get_all()) == 14
    random.seed(100)
    event_service.add_random_events(20)
    assert event_service.search_by_id(14).get_duration() == time(16, 8)
    assert len(event_service.get_all()) == 19
