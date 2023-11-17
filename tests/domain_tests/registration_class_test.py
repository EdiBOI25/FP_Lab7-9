from domain.person import Person
from domain.event import Event
from domain.registration import Registration
from datetime import date, time


def test_registration():
    person = Person(1, 'Bob', 'Brasov')
    event = Event(1, date(2020, 2, 3), time(2, 30), 'lol')
    registration = Registration(person, event)
    assert registration.get_event() == Event(1, date(2020, 2, 3), time(2, 30), 'lol')
    assert registration.get_person() == Person(1, 'Bob', 'Brasov')
    registration.set_event(Event(2, date(2021, 2, 3), time(2, 30), 'lol22'))
    assert registration.get_event() == Event(2, date(2021, 2, 3), time(2, 30), 'lol22')
    registration.set_person(Person(2, 'Bob2', 'Brasov2'))
    assert registration.get_person() == Person(2, 'Bob2', 'Brasov2')
