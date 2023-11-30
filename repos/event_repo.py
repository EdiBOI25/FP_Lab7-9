from validators.event_validator import *


class EventRepository:
    def __init__(self, ev_f):
        self.__event_list = []
        self.__validator = EventValidator()

    def __str__(self):
        string = ''
        for event in self.__event_list:
            string += str(event)
            string += '\n'
        return string

    def __len__(self):
        """
        :return: Returneaza lungimea listei
        """
        return len(self.__event_list)

    def get_all(self):
        """
        :return: returneaza lista
        """
        return self.__event_list

    # def __getitem__(self, index):
    #     return self.__event_list[index]

    def is_id_in_list(self, idcode):
        """
        Verifica daca id-ul se afla in lista
        :param idcode:
        :return: True/False
        """
        for event in self.__event_list:
            if event.get_id() == idcode:
                return True
        return False

    def add_event(self, event: Event):
        """
        Adauga un eveniment in lista
        :param event: Obiect de tip Event
        """
        self.__validator.validate_event(event)
        if self.is_id_in_list(event.get_id()):
            raise ValueError(f'Evenimentul cu id-ul {event.get_id()} se afla deja in lista')
        self.__event_list.append(event)

    def remove_event(self, event: Event):
        """
        Sterge un eveniment din lista de evenimente
        :param event: Obiect de tip Event
        """
        if event in self.__event_list:
            self.__event_list.remove(event)
            return
        raise ValueError(f'Evenimentul pe care vrei sa il stergi nu se afla in lista.')

    def search_event_by_id(self, idcode) -> Event:
        """
        Cauta un eveniment dupa ID in lista de evenimente si il returneaza
        :param idcode: ID-ul dupa care cautam
        :return: evenimentul cautat
        """
        for event in self.__event_list:
            if event.get_id() == idcode:
                return event
        raise ValueError(f'Nu exista evenimentul cu id-ul {idcode} in lista')

    def update_event(self, id_code, new_date, new_duration, new_description):
        """
        Modifica datele evenimentului cu id-ul id_code
        :param id_code: id-ul evenimentului pe care vrem sa il modificam
        :param new_date: data noua
        :param new_duration: durata noua
        :param new_description: descrierea noua
        :return:
        """
        for event in self.__event_list:
            if id_code == event.get_id():
                new_event = Event(id_code, new_date, new_duration, new_description)
                self.__validator.validate_event(new_event)
                index = self.__event_list.index(event)
                self.__event_list[index] = new_event
                return

        raise ValueError(f'Evenimentul cu id-ul {id_code} nu se afla in lista.')
