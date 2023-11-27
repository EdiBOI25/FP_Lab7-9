from repos.registration_repo import RegistrationRepo
from utils.general_utils import sort_event_list_by_description, sort_event_list_by_date
from collections import Counter


class RegistrationService:
    def __init__(self):
        self.__repo = RegistrationRepo()

    def get_all(self):
        return self.__repo.get_all()

    def __str__(self):
        return str(self.__repo)

    def add_registration(self, person_id, event_id):
        """
        Adauga inscriere
        :param person_id:
        :param event_id:
        :return:
        """
        if self.search_registration(person_id, event_id):
            raise ValueError('Inscrierea este deja inregistrata.')
        self.__repo.add_registration(person_id, event_id)

    def remove_registration(self, person_id, event_id):
        """
        Sterge inscriere
        :param person_id:
        :param event_id:
        :return:
        """
        self.__repo.remove_registration(person_id, event_id)

    def search_registration(self, person_id, event_id):
        """
        Cauta inscrierea
        :param person_id:
        :param event_id:
        :return:
        """
        return self.__repo.search_registration(person_id, event_id)

    def get_events_of_person(self, person_id):
        """
        Returneaza evenimentele la care este inscrisa o persoana
        :param person_id:
        :return:
        """
        return self.__repo.get_events_of_person(person_id)

    def get_people_of_event(self, event_id):
        """
        Returneaza persoanele inscrise la un eveniment
        :param event_id:
        :return:
        """
        return self.__repo.get_people_of_event(event_id)

    def get_events_sorted_by_description(self, person_id, event_list):
        result = self.get_events_of_person(person_id)
        # print(f'Lista initiala e: {result}')
        result = list(map(lambda evid: event_list.search_by_id(evid), result))
        # print(f'Lista de evenimente e: {result}')
        return sort_event_list_by_description(result)

    def get_events_sorted_by_date(self, person_id, event_list):
        result = self.get_events_of_person(person_id)
        # print(f'Lista initiala e: {result}')
        result = list(map(lambda evid: event_list.search_by_id(evid), result))
        # print(f'Lista de evenimente e: {result}')
        return sort_event_list_by_date(result)

    def most_attending_people(self):
        """
        Returneaza persoanele inscrise la cele mai multe evenimente
        :return:
        """
        per_id_list = list(map(lambda reg: reg.get_person(), self.__repo.get_all()))
        if not per_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        freq_dict = {}
        result = []
        for num in per_id_list:
            if num not in freq_dict:
                freq_dict[num] = len(self.get_events_of_person(num))
        max_freq = freq_dict[max(freq_dict, key=lambda per: freq_dict[per])]
        for num in freq_dict:
            if freq_dict[num] == max_freq:
                result.append(num)
        return result

    def most_attended_events(self):
        """
        Returneaza evenimentele sortate dupa nr de participanti
        :return:
        """
        ev_id_list = list(map(lambda reg: reg.get_event(), self.__repo.get_all()))
        if not ev_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        freq_dict = {}
        result = []
        for num in ev_id_list:
            if num not in freq_dict:
                freq_dict[num] = len(self.get_people_of_event(num))
        freq_dict = sorted(freq_dict, key=lambda ev: freq_dict[ev], reverse=True)
        for num in freq_dict:
            result.append(num)
        return result

    def attended_event_counter(self):
        """
        Returneaza numarul de evenimente care au macar o persoana inscrisa
        :return:
        """
        ev_id_list = list(map(lambda reg: reg.get_event(), self.__repo.get_all()))
        if not ev_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        result = []
        for ev in ev_id_list:
            if ev not in result:
                result.append(ev)
        return len(result)
