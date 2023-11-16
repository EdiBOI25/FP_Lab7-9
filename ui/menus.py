class Menus:
    def __init__(self):
        self.__main_menu = '''
    MENIU PRINCIPAL
    1. Gestioneaza lista de persoane
    2. Gestioneaza lista de evenimente
    9. Printeaza listele
    0. Iesi
    '''
        self.__person_menu = '''
    GESTIONEAZA LISTA DE PERSOANE:
    1. Adauga persoana
    2. Modifica persoana
    3. Sterge persoana
    4. Cauta persoana dupa ID
    9. Afiseaza lista de persoane
    0. Inapoi
    '''
        self.__event_menu = '''
    GESTIONEAZA LISTA DE EVENIMENTE:
    1. Adauga eveniment
    2. Modifica eveniment
    3. Sterge eveniment
    4. Cauta eveniment dupa ID
    9. Afiseaza lista de evenimente
    0. Inapoi
    '''

    def get_main_menu(self):
        return self.__main_menu

    def get_person_menu(self):
        return self.__person_menu

    def get_event_menu(self):
        return self.__event_menu
