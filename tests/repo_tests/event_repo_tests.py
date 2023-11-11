from repos.event_repo import EventRepository
from domain.event import Event
from datetime import date, time


def test_event_repo():
    event_list = EventRepository()

    untold = Event(1234, date(2020, 12, 8), time(1, 20), 'Best festival ever')
    # add_event test
    try:
        event_list.add_event(untold)
        assert True
    except ValueError:
        assert False
    try:
        event_list.add_event(Event('', date(2020, 12, 8), time(1, 20), 'Best festival ever'))
        assert False
    except ValueError:
        assert True
    try:
        event_list.add_event(Event(1234, date(2020, 12, 8), time(1, 20), 'Best festival ever'))
        assert False
    except ValueError:
        assert True

    # remove_event test
    electric = Event(2525, date(2020, 12, 8), time(1, 20), 'Best festival ever')
    event_list.add_event(electric)
    neverc = Event(1236, date(2020, 12, 8), time(1, 20), 'Best festival ever')
    event_list.add_event(neverc)
    try:
        event_list.remove_event(electric)
        assert True
    except ValueError:
        assert False
    try:
        event_list.remove_event(Event(2525, date(2021, 12, 8), time(1, 20), 'Best festival ever'))
        assert False
    except ValueError:
        assert True

    # search_event_by_id test
    try:
        result = event_list.search_event_by_id(1236)
        assert True
    except ValueError:
        assert False
    try:
        result = event_list.search_event_by_id(6541)
        assert False
    except ValueError:
        assert True

    # update_event test
    event_list.add_event(electric)
    try:
        event_list.update_event(electric, Event(2525, date(2020, 12, 8), time(1, 20), 'Best festival ever222'))
        assert True
    except ValueError:
        assert False
    try:
        event_list.update_event(electric, Event(1236, date(2020, 12, 8), time(1, 20), 'Best festival ever'))
        assert False
    except ValueError:
        assert True
    try:
        event_list.update_event(Event(976, date(2020, 12, 8), time(1, 20), 'Best festival ever'),
                                Event(2525, date(2020, 12, 8), time(1, 20), 'Best festival ever'))
        assert False
    except ValueError:
        assert True
    try:
        event_list.update_event(electric, untold)
        assert False
    except ValueError:
        assert True
    try:
        event_list.update_event_id(electric, 1236)
        assert False
    except ValueError:
        assert True
    try:
        event_list.update_event_id(event_list.search_event_by_id(1236), 4200)
        event_list.update_event_date(event_list.search_event_by_id(4200), date(2021, 4, 1))
        event_list.update_event_duration(event_list.search_event_by_id(4200), time(1, 40, 30))
        event_list.update_event_description(event_list.search_event_by_id(4200), 'Worst festival ever :(')
        assert True
    except ValueError:
        assert False
