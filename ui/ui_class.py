from service.event_service import EventService
from service.person_service import PersonService
from ui.menus import Menus
from datetime import date, time


class UI:
    def __init__(self):
        self.__person_service = PersonService()
        self.__event_service = EventService()
        # self.__register_service = RegisterService()
        self.__menus = Menus()

    # menu printers
    def __print_main_menu(self):
        print(self.__menus.get_main_menu())

    def __print_person_menu(self):
        print(self.__menus.get_person_menu())

    def __print_event_menu(self):
        print(self.__menus.get_event_menu())

    # data validators
    @staticmethod
    def __read_valid_int(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print('Valoarea introdusa nu e numar intreg. Incearca din nou')

    @staticmethod
    def __read_nonempty_string(message):
        while True:
            try:
                string = input(message)
                if not string:
                    raise ValueError
                return string
            except ValueError:
                print('String-ul nu poate fi gol')

    def __read_valid_date(self):
        while True:
            try:
                year = self.__read_valid_int('An: ')
                month = self.__read_valid_int('Luna: ')
                day = self.__read_valid_int('Zi: ')
                return date(year, month, day)
            except ValueError as e:
                print(str(e))

    def __read_valid_time(self):
        while True:
            try:
                hours = self.__read_valid_int('Ore: ')
                minutes = self.__read_valid_int('Minute: ')
                return time(hours, minutes)
            except ValueError as e:
                print(str(e))

    # person methods
    def __add_person(self):
        name = self.__read_nonempty_string('Numele: ')
        address = self.__read_nonempty_string('Adresa: ')
        try:
            self.__person_service.add_person(name, address)
            print(f'Persoana a fost adaugata cu succes!')
        except Exception as e:
            print(e)

    def __remove_person(self):
        idcode = self.__read_valid_int('ID-ul persoanei: ')
        try:
            self.__person_service.remove_person(idcode)
            print('Persoana a fost stersa cu succes!')
        except Exception as e:
            print(e)

    def __update_person(self):
        idcode = self.__read_valid_int('ID-ul persoanei: ')
        try:
            person = self.__person_service.search_by_id(idcode)
            print(f'Persoana careia vrei sa ii modifici datele este {person}')
        except Exception as e:
            print(e)
            return
        new_name = self.__read_nonempty_string('Numele nou: ')
        new_address = self.__read_nonempty_string('Adresa noua: ')
        try:
            self.__person_service.update_person(idcode, new_name, new_address)
            print(f'Datele persoanei au fost modificate: {self.__person_service.search_by_id(idcode)}')
        except Exception as e:
            print(e)

    def __find_person(self):
        idcode = self.__read_valid_int('ID-ul persoanei: ')
        try:
            person = self.__person_service.search_by_id(idcode)
            print(f'Persoana cautata este {person}')
        except Exception as e:
            print(e)

    # event methods
    def __add_event(self):
        start_date = self.__read_valid_date()
        duration = self.__read_valid_time()
        description = self.__read_nonempty_string('Descriere: ')
        try:
            self.__event_service.add_event(start_date, duration, description)
            print(f'Evenimentul a fost adaugat cu succes!')
        except Exception as e:
            print(f'Something went wrong: {e}')

    def __remove_event(self):
        idcode = self.__read_valid_int('ID-ul evenimentului: ')
        try:
            self.__event_service.remove_event(idcode)
            print('Evenimentul a fost sters cu succes!')
        except Exception as e:
            print(e)

    def __update_event(self):
        idcode = self.__read_valid_int('ID-ul evenimentului: ')
        try:
            event = self.__event_service.search_by_id(idcode)
            print(f'Evenimentul caruia vrei sa ii modifici datele este {event}')
        except Exception as e:
            print(e)
            return
        new_date = self.__read_valid_date()
        new_duration = self.__read_valid_time()
        new_description = self.__read_nonempty_string('Descriere: ')
        try:
            self.__event_service.update_event(idcode, new_date, new_duration, new_description)
            print(f'Datele evenimentului au fost modificate: {self.__event_service.search_by_id(idcode)}')
        except Exception as e:
            print(e)

    def __find_event(self):
        idcode = self.__read_valid_int('ID-ul evenimentului: ')
        try:
            event = self.__event_service.search_by_id(idcode)
            print(f'Evenimentul cautat este: {event}')
        except Exception as e:
            print(e)

    # main UI
    def __manage_person(self):
        while True:
            self.__print_person_menu()
            option = self.__read_valid_int('Introdu optiunea: ')
            if option == 1:
                self.__add_person()
            elif option == 2:
                self.__update_person()
            elif option == 3:
                self.__remove_person()
            elif option == 4:
                self.__find_person()
            elif option == 9:
                if self.__person_service.get_all():
                    print(self.__person_service)
                else:
                    print('Lista de persoane este goala.')
            elif option == 0:
                return
            else:
                print('Optiune invalida')

    def __manage_event(self):
        while True:
            self.__print_event_menu()
            option = self.__read_valid_int('Introdu optiunea: ')
            if option == 1:
                self.__add_event()
            elif option == 2:
                self.__update_event()
            elif option == 3:
                self.__remove_event()
            elif option == 4:
                self.__find_event()
            elif option == 0:
                return
            elif option == 9:
                if self.__event_service.get_all():
                    print(self.__event_service)
                else:
                    print('Lista de evenimente este goala.')
            else:
                print('Optiune invalida')

    def __manage_register(self):
        pass

    def __reports(self):
        pass

    def run(self):
        while True:
            self.__print_main_menu()
            option = self.__read_valid_int('Introdu optiunea: ')
            if option == 1:
                self.__manage_person()
            elif option == 2:
                self.__manage_event()
            elif option == 9:
                if self.__person_service.get_all():
                    print('Persoane:\n', self.__person_service)
                else:
                    print('Lista de persoane este goala.')
                if self.__event_service.get_all():
                    print('Evenimente:\n', self.__event_service)
                else:
                    print('Lista de evenimente este goala.')
            elif option == 0:
                print('Bye bye!')
                return
            else:
                print('Optiune invalida')
