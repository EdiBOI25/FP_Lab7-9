class Event:
    def __init__(self, event_id: str, date, duration, description: str):
        self.__id = event_id
        self.__date = date
        self.__duration = duration
        self.__description = description

    def get_id(self):
        return self.__id

    def get_date(self):
        return self.__date

    def get_duration(self):
        return self.__duration

    def get_description(self):
        return self.__description

    def set_id(self, new_id):
        self.__id = new_id

    def set_date(self, new_date):
        self.__date = new_date

    def set_duration(self, new_duration):
        self.__duration = new_duration

    def set_description(self, new_description):
        self.__description = new_description
