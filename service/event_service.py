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
