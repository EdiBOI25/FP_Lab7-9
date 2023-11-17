from domain.person import Person
from domain.event import Event
from domain.registration import Registration
from datetime import date, time


def test_registration():
    person = Person(1, 'Bob', 'Brasov')
    event = Event(1, date(2020, 2, 3), time(2, 30), 'lol')
    registration = Registration(person.get_id(), event.get_id())
    assert registration.get_event() == 1
    assert registration.get_person() == 1
    registration.set_event(2)
    assert registration.get_event() == 2
    registration.set_person(2)
    assert registration.get_person() == 2
