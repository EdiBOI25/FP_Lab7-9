from service.registration_service import RegistrationService


def test_registration_service():
    reg_service = RegistrationService()
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
