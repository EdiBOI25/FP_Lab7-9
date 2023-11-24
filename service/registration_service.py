from repos.registration_repo import RegistrationRepo
from utils.general_utils import sort_event_list_by_description


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

    def get_persons_of_event(self, event_id):
        """
        Returneaza persoanele inscrise la un eveniment
        :param event_id:
        :return:
        """
        return self.__repo.get_persons_of_event(event_id)

    def get_events_sorted_by_description(self, person_id, event_list):
        result = self.get_events_of_person(person_id)
        # print(f'Lista initiala e: {result}')
        result = list(map(lambda evid: event_list.search_by_id(evid), result))
        # print(f'Lista de evenimente e: {result}')
        return sort_event_list_by_description(result)
