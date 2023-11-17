from repos.event_repo import *
from utils import general_utils


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
