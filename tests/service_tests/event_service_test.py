from service.event_service import *
from datetime import date, time


def test_event_service():
    event_service = EventService()
    assert event_service.get_all() == []
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
