class Registration:
    def __init__(self, person_id: int, event_id: int):
        self.__person_id = person_id
        self.__event_id = event_id

    def __eq__(self, other):
        if not isinstance(other, Registration):
            return False
        return (self.__person_id == other.get_person() and
                self.__event_id == self.get_event())

    def __str__(self):
        return f'Registration(PersonID:{self.__person_id}, EventID:{self.__event_id})'

    def get_person(self):
        return self.__person_id

    def get_event(self):
        return self.__event_id

    def set_person(self, new_id):
        self.__person_id = new_id

    def set_event(self, new_id):
        self.__event_id = new_id
