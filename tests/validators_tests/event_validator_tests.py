from validators.event_validator import EventValidator, Event
from datetime import date, time


def test_event_validator():
    untold = Event(123, date(2023, 8, 12), time(1, 20), 'Biggest festival')
    validator = EventValidator()
    try:
        validator.validate_event(untold)
        assert True
    except ValueError:
        assert False

    try:
        untold.set_id('')
        validator.validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_date('')
        validator.validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_duration('')
        validator.validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_date('')
        validator.validate_event(untold)
        assert False
    except ValueError:
        assert True

    try:
        untold.set_description('')
        validator.validate_event(untold)
        assert False
    except ValueError:
        assert True
