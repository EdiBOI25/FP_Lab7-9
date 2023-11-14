from tests.test_main import execute_all_tests
from ui.sub_mains import *

# TODO: de facut parea de ui, macar un pic


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
