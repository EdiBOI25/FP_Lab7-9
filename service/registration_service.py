from repos.registration_repo import RegistrationRepo
from utils.general_utils import sort_event_list_by_description, sort_event_list_by_date


class RegistrationService:
    def __init__(self, reg_f):
        self.__repo = RegistrationRepo(reg_f)

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

    def most_attended_events_20percent(self, event_list):
        """
        Returneaza evenimentele sortate dupa nr de participanti
        :return:
        """
        # lista cu toate id-urile din registration_list
        ev_id_list = list(map(lambda reg: reg.get_event(), self.__repo.get_all()))
        # numarul de evenimente (fara sa se repete)
        ev_num = self.attended_event_counter()
        if not ev_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        freq_dict = {}
        result = []
        # pt fiecare id de eveniment punem numarul de participanti
        for num in ev_id_list:
            if num not in freq_dict:
                freq_dict[num] = len(self.get_people_of_event(num))
        # lista sortata cu id-urile
        freq_list = sorted(freq_dict, key=lambda ev: freq_dict[ev], reverse=True)
        for num in freq_list:
            result.append(f'{event_list.search_by_id(num).get_description()}, Nr Participanti: {freq_dict[num]}')
        return result[:ev_num//5]

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

    def least_attending_people_80percent(self, person_list):
        """
        Returneaza persoanele sortate dupa nr de evenimente la care sunt inscrise
        :return:
        """
        per_id_list = list(map(lambda reg: reg.get_person(), self.__repo.get_all()))
        per_num = self.attending_people_counter()
        if not per_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        freq_dict = {}
        result = []
        for num in per_id_list:
            if num not in freq_dict:
                freq_dict[num] = len(self.get_events_of_person(num))
        freq_list = sorted(freq_dict, key=lambda per: freq_dict[per], reverse=False)
        for num in freq_list:
            result.append(f'{person_list.search_by_id(num).get_name()}, participa la: {freq_dict[num]} evenimente')
        return result[:per_num * 4 // 5]

    def attending_people_counter(self):
        """
        Returneaza numarul de persoane care sunt inscrise la macar un eveniment
        :return:
        """
        per_id_list = list(map(lambda reg: reg.get_person(), self.__repo.get_all()))
        if not per_id_list:
            raise ValueError('Nicio persoana nu s-a inscris la niciun eveniment')
        result = []
        for per in per_id_list:
            if per not in result:
                result.append(per)
        return len(result)
