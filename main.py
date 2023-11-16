from tests.test_main import execute_all_tests
from ui.sub_mains import *

# TODO: fa UI
# TODO 2: extinde service
# TODO 3: fa un "register" repo care sa contina o lista de perechi de genu (id_client, id_event) si sterge
#   lista de eventuri/persoane din clasele person/event
# TODO 4: refa testele astfel incat la erori sa faci assert err == 'Asta e eroarea', adauga comentarii la functii
# TODO 5: fa cerintele alealalte (rapoarte etc)


option_list = {
    1: manage_person_list,
    2: manage_event_list,
}


def main():
    person_list = PersonRepository()
    event_list = EventRepository()
    while True:
        print_main_menu()
        option = int(input('Alege o optiune: '))

        if option == 1:
            manage_person_list(person_list)
        elif option == 2:
            manage_event_list(event_list)
        elif option == 9:
            print('Lista de persoane:')
            print(person_list)
            print('Lista de evenimente: ')
            print(event_list)
        elif option == 0:
            print('bye bye')
            return


if __name__ == '__main__':
    execute_all_tests()
    main()
