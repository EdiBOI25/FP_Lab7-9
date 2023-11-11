from validators.event_validator import *


class EventRepository:
    def __init__(self):
        self.__event_list = []

    def get_event_list(self):
        return self.__event_list

    def __getitem__(self, index):
        return self.__event_list[index]

    def add_event(self, event: Event):
        """
        Adauga un eveniment in lista
        :param event: Obiect de tip Event
        """
        validate_event(event)
        for ev in self.__event_list:
            if event.get_id() == ev.get_id():
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

    def update_event(self, event: Event, new_event: Event):
        """
        Modifica datele unui eveniment
        :param new_event: Obiect eveniment cu datele modificate
        :param event: Evenimentul caruia vrem sa ii modificam datele
        :return:
        """
        validate_event(new_event)
        if event not in self.__event_list:
            raise ValueError(f'Evenimentul caruia vrei sa ii modifici datele nu se afla in lista.')
        index = self.__event_list.index(event)
        self.__event_list[index] = new_event

    def update_event_id(self, event: Event, new_id):
        self.update_event(event, Event(new_id, event.get_date(), event.get_duration(), event.get_description()))

    def update_event_date(self, event: Event, new_date):
        self.update_event(event, Event(event.get_id(), new_date, event.get_duration(), event.get_description()))

    def update_event_duration(self, event: Event, new_duration):
        self.update_event(event, Event(event.get_id(), event.get_date(), new_duration, event.get_description()))

    def update_event_description(self, event: Event, new_desc):
        self.update_event(event, Event(event.get_id(), event.get_date(), event.get_duration(), new_desc))
