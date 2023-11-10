from validators.event_validator import *
from datetime import date, time


def test_event_validator():
    untold = Event(123, date(2023, 8, 12), time(1, 20), 'Biggest festival')
    try:
        validate_event(untold)
        assert True
    except ValueError:
        assert False

    try:
        untold.set_id('')
        validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_date('')
        validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_duration('')
        validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_date('')
        validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_description('')
        validate_event(untold)
        assert False
    except ValueError:
        assert True
