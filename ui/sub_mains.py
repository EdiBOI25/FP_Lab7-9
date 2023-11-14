from ui.menus import *
from repos.person_repo import *
from repos.event_repo import *
from datetime import date, time


def manage_person_list(person_list):
    print_person_list_menu()
    option = int(input('Alege o optiune: '))
    if option == 1:
        while True:
            try:
                idcode = int(input('Introdu ID-ul: '))
                name = input('Introdu numele: ')
                address = input('Introdu adresa: ')
                person_list.add_person(Person(idcode, name, address))
                break
            except ValueError as e:
                print(e)
                print('Incearca din nou.')


def manage_event_list(event_list):
    print_event_list_menu()
    option = int(input('Alege o optiune: '))
    if option == 1:
        while True:
            try:
                idcode = int(input('Introdu ID-ul:'))
                start_date = date(
                    int(input('Introdu anul: ')),
                    int(input('Introdu luna: ')),
                    int(input('Introdu ziua: '))
                )
                duration = time(
                    int(input('Introdu ora: ')),
                    int(input('Introdu minutele: '))
                )
                description = input('Introdu o descriere: ')
                event_list.add_event(Event(idcode, start_date, duration, description))
                break
            except ValueError as e:
                print(e)
                print('Incearca din nou')
