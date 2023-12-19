from service.registration_service import RegistrationService
from service.person_service import PersonService
from service.event_service import EventService
import random


def test_registration_service():
    person_file = 'tests/service_tests/people.txt'
    open(person_file, 'w').close()
    event_file = 'tests/service_tests/events.txt'
    open(event_file, 'w').close()
    reg_file = 'tests/service_tests/registrations.txt'
    open(reg_file, 'w').close()
    reg_service = RegistrationService(reg_file)
    per_service = PersonService(person_file)
    ev_service = EventService(event_file)

    per_service.add_random_people(50)
    ev_service.add_random_events(50)

    reg_service.add_registration(1, 1)
    reg_service.add_registration(1, 2)
    reg_service.add_registration(1, 4)
    reg_service.add_registration(2, 1)
    reg_service.add_registration(2, 4)
    reg_service.add_registration(3, 3)
    reg_service.add_registration(3, 1)
    reg_service.add_registration(3, 2)
    assert reg_service.get_events_of_person(1) == [1, 2, 4]
    try:
        res = reg_service.get_events_of_person(4)
        assert False
    except ValueError as e:
        assert str(e) == 'Persoana cu ID-ul 4 nu s-a inscris la niciun eveniment'
    assert reg_service.get_people_of_event(4) == [1, 2]
    try:
        res = reg_service.get_people_of_event(6)
        assert False
    except ValueError as e:
        assert str(e) == 'Evenimentul cu ID-ul 6 nu are persoane inscrise'
    try:
        reg_service.remove_registration(6, 7)
        assert False
    except ValueError as e:
        assert str(e) == 'Persoana cu ID-ul 6 nu este inscrisa la evenimentul cu ID-ul 7'
    reg_service.add_registration(3, 20)
    reg_service.add_registration(1, 20)
    reg_service.add_registration(1, 21)
    reg_service.add_registration(1, 22)
    reg_service.add_registration(1, 23)
    reg_service.add_registration(1, 24)
    reg_service.add_registration(3, 21)
    assert reg_service.most_attending_people() == [1]
    # print(reg_service)
    # print(per_service)
    # print(ev_service)
    assert reg_service.most_attended_events_20percent(ev_service) == ['izwxsnsgjizamhiioilknkowpxossm, Nr Participanti: 3']
    assert reg_service.least_attending_people_80percent(per_service) == [
        'Cpbnmegnfgiigjmmikax, participa la: 2 evenimente',
        'Kpymtnhypxdqgfchcatz, participa la: 5 evenimente'
    ]
