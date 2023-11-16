from datetime import date, time


class Event:
    def __init__(self, event_id: int, start_date: date, duration: time, description: str):
        self.__id = event_id
        self.__date = start_date
        self.__duration = duration
        self.__description = description

    def __eq__(self, other):
        if not isinstance(other, Event):
            return False
        return self.__id == other.get_id()

    def __str__(self):
        return f'Event(ID: {self.__id}, Data: {self.__date}, Durata: {self.__duration}, Descriere: {self.__duration})\nLista de participanti: {self.__attendants_list}'

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_duration(self):
        return self.__duration

    def get_description(self):
        return self.__description

    def set_id(self, new_id: int):
        self.__id = new_id

    def set_date(self, new_date: date):
        self.__date = new_date

    def set_duration(self, new_duration: time):
        self.__duration = new_duration

    def set_description(self, new_description: str):
        self.__description = new_description
