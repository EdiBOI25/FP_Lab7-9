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

    def add_registration(self, person_id, event_id):
        new_registration = Registration(person_id, event_id)
        self.__registration_list.append(new_registration)

    def remove_registration(self, person_id, event_id):
        for reg in self.__registration_list:
            if reg.get_person() == person_id and reg.get_event() == event_id:
                self.__registration_list.remove(reg)
                return
        raise ValueError(f'Persoana cu ID-ul {person_id} nu este inscrisa la evenimentul cu ID-ul {event_id}')
