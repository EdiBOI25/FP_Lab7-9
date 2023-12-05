from validators.event_validator import *
from datetime import date, time


class EventFileRepository:
    def __init__(self, file_name):
        self.__validator = EventValidator()
        self.__file_name = file_name

    @staticmethod
    def __date_from_str(string):
        split_str = string.split('-')
        year = int(split_str[0])
        month = int(split_str[1])
        day = int(split_str[2])
        return date(year, month, day)

    @staticmethod
    def __time_from_str(string):
        split_str = string.split(':')
        hours = int(split_str[0])
        minutes = int(split_str[1])
        return time(hours, minutes)

    def load_from_file(self):
        """
        Ia datele evenimentelor din fisier
        :return: lista de evenimente
        """
        with open(self.__file_name, 'r') as file:
            line = file.readline().strip()
            result = []
            while line != '':
                params = line.split(',')
                start_date = self.__date_from_str(params[1])
                duration = self.__time_from_str(params[2])
                event = Event(int(params[0]), start_date, duration, params[3])
                result.append(event)
                line = file.readline().strip()
        return result

    def store_to_file(self, ev_list):
        """
        Stocheaza lista transmisa in fisier
        :param ev_list:
        :return:
        """
        with open(self.__file_name, 'w') as file:
            for ev in ev_list:
                str_ev = str(ev.get_id()) + ',' + str(ev.get_date()) + ',' + str(ev.get_duration()) + ',' + ev.get_description() + '\n'
                file.write(str_ev)
