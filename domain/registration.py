from domain.event import Event
from domain.person import Person


class Registration:
    def __init__(self, person: Person, event: Event):
        self.__person = person
        self.__event = event

    def __eq__(self, other):
        if not isinstance(other, Registration):
            return False
        return (self.__person.get_id() == other.get_person().get_id() and
                self.__event.get_id() == self.get_event().get_id())

    def __str__(self):
        return f'Registration({self.__person}, {self.__event})'

    def get_person(self):
        return self.__person

    def get_event(self):
        return self.__event

    def set_person(self, new_person: Person):
        self.__person = new_person

    def set_event(self, new_event: Event):
        self.__event = new_event
