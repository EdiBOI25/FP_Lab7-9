from domain.registration import Registration


class RegistrationRepo:
    def __init__(self):
        self.__registration_list = []

    def __str__(self):
        string = ''
        for reg in self.__registration_list:
            string += str(reg)
            string += '\n'
        return string

    def __len__(self):
        return len(self.__registration_list)

    def get_all(self):
        return self.__registration_list

    def __getitem__(self, index):
        return self.__registration_list[index]

    def __is_person_in_list(self, person_id):
        for reg in self.__registration_list:
            if reg.get_person() == person_id:
                return True
        return False

    def __is_event_in_list(self, event_id):
        for reg in self.__registration_list:
            if reg.get_event() == event_id:
                return True
        return False

    def get_events_of_person(self, person_id):
        if not self.__is_person_in_list(person_id):
            raise ValueError(f'Persoana cu ID-ul {person_id} nu s-a inscris la niciun eveniment')
        result = []
        for reg in self.__registration_list:
            if reg.get_person() == person_id:
                result.append(reg.get_event())
        return result

    def get_persons_of_event(self, event_id):
        if not self.__is_event_in_list(event_id):
            raise ValueError(f'Evenimentul cu ID-ul {event_id} nu are persoane inscrise')
        result = []
        for reg in self.__registration_list:
            if reg.get_event() == event_id:
                result.append(reg.get_person())
        return result

    def add_registration(self, person_id, event_id):
        new_registration = Registration(person_id, event_id)
        self.__registration_list.append(new_registration)

    def remove_registration(self, person_id, event_id):
        for reg in self.__registration_list:
            if reg.get_person() == person_id and reg.get_event() == event_id:
                self.__registration_list.remove(reg)
                return
        raise ValueError(f'Persoana cu ID-ul {person_id} nu este inscrisa la evenimentul cu ID-ul {event_id}')
