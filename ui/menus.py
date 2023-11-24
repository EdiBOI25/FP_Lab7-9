class Menus:
    def __init__(self):
        self.__main_menu = '''
    MENIU PRINCIPAL
    1. Gestioneaza lista de persoane
    2. Gestioneaza lista de evenimente
    3. Gestioneaza inscrierile
    4. Rapoarte
    9. Printeaza listele
    0. Iesi
    '''
        self.__person_menu = '''
    GESTIONEAZA LISTA DE PERSOANE:
    1. Adauga persoana
    2. Modifica persoana
    3. Sterge persoana
    4. Cauta persoana dupa ID
    5. Adauga un numar random de persoane random
    9. Afiseaza lista de persoane
    0. Inapoi
    '''
        self.__event_menu = '''
    GESTIONEAZA LISTA DE EVENIMENTE:
    1. Adauga eveniment
    2. Modifica eveniment
    3. Sterge eveniment
    4. Cauta eveniment dupa ID
    5. Adauga un numar random de evenimente random
    9. Afiseaza lista de evenimente
    0. Inapoi
    '''
        self.__registration_menu = '''
    GESTIONEAZA INSCRIERILE
    1. Inscrie persoana la eveniment
    2. Sterge o inscriere
    3. Afiseaza evenimentele la care este inscrisa o persoana
    4. Afiseaza persoanele care sunt inscrise la un eveniment
    9. Afiseaza lista de inregistrari
    0. Inapoi
        '''
        self.__reports_menu = '''
    MENIU DE RAPOARTE:
    1. Afiseaza lista de evenimente la care participă o persoană ordonat alfabetic după descriere
    2. Afiseaza lista de evenimente la care participă o persoană ordonat dupa data
    2. Afiseaza persoanele participante la cele mai multe evenimente
    3. Afiseaza primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți)
    0. Inapoi
        '''

    def get_main_menu(self):
        return self.__main_menu

    def get_person_menu(self):
        return self.__person_menu

    def get_event_menu(self):
        return self.__event_menu

    def get_registration_menu(self):
        return self.__registration_menu

    def get_reports_menu(self):
        return self.__reports_menu
