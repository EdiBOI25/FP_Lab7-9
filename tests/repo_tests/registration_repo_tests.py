from repos.registration_repo import RegistrationRepo, RegistrationFileRepository, Registration


def test_registration_repo():
    registrations_file = 'tests/repo_tests/registrations.txt'
    try:
        RegistrationFileRepository('text.txt').load_from_file()
        assert False
    except FileNotFoundError as e:
        assert str(e) == '[Errno 2] No such file or directory: \'text.txt\''
    open(registrations_file, 'w').close()
    assert RegistrationFileRepository(registrations_file).load_from_file() == []
    lst = [
        Registration(1, 2),
        Registration(3, 4)
    ]
    RegistrationFileRepository(registrations_file).store_to_file(lst)
    assert RegistrationFileRepository(registrations_file).load_from_file() == [
        Registration(1, 2),
        Registration(3, 4)
    ]

    open(registrations_file, 'w').close()
    reg_list = RegistrationRepo(registrations_file)
    reg_list.add_registration(1, 1)
    reg_list.add_registration(1, 2)
    reg_list.add_registration(1, 4)
    reg_list.add_registration(2, 1)
    reg_list.add_registration(2, 4)
    reg_list.add_registration(3, 3)
    assert len(reg_list) == 6
    assert reg_list.get_events_of_person(1) == [1, 2, 4]
    try:
        res = reg_list.get_events_of_person(4)
        assert False
    except ValueError as e:
        assert str(e) == 'Persoana cu ID-ul 4 nu s-a inscris la niciun eveniment'
    assert reg_list.get_people_of_event(4) == [1, 2]
    try:
        res = reg_list.get_people_of_event(6)
        assert False
    except ValueError as e:
        assert str(e) == 'Evenimentul cu ID-ul 6 nu are persoane inscrise'
    try:
        reg_list.remove_registration(6, 7)
        assert False
    except ValueError as e:
        assert str(e) == 'Persoana cu ID-ul 6 nu este inscrisa la evenimentul cu ID-ul 7'
