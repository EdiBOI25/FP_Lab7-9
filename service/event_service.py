import string

from repos.event_repo import *
from utils import general_utils
import random
from datetime import date, time


class EventService:
    def __init__(self):
        self.__repo = EventRepository()

    def get_all(self):
        return self.__repo.get_all()

    def __str__(self):
        return str(self.__repo)

    def add_event(self, date, duration, description):
        idcode = general_utils.generate_id(self.__repo.get_all())
        self.__repo.add_event(Event(idcode, date, duration, description))
        
    def remove_event(self, idcode):
        event = self.search_by_id(idcode)
        self.__repo.remove_event(event)

    def search_by_id(self, idcode):
        return self.__repo.search_event_by_id(idcode)

    def update_event(self, idcode, new_date, new_duration, new_description):
        self.__repo.update_event(idcode, new_date, new_duration, new_description)

    @staticmethod
    def __random_date():
        year = random.randint(2000, 2030)
        month = random.randint(1, 12)
        while True:
            try:
                day = random.randint(1, 31)
                break
            except ValueError:
                pass
        return date(year, month, day)

    @staticmethod
    def __random_time():
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)
        return time(hour, minute)

    @staticmethod
    def __random_string(max_length):
        rand_string = ''
        for i in range(max_length):
            rand_string += random.choice(string.ascii_lowercase)
        return rand_string

    def add_random_events(self, limit):
        """
        Adds a random number of random events
        :param limit: The max number of events to add
        :return:
        """
        num = random.randint(1, limit)
        for i in range(1, num + 1):
            start_date = self.__random_date()
            duration = self.__random_time()
            description = self.__random_string(30)
            self.add_event(start_date, duration, description)
