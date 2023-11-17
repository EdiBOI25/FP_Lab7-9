from domain.registration import Registration
from repos.person_repo import PersonRepository
from repos.event_repo import EventRepository


class RegistrationValidator:
    def __init__(self, person_repo, event_repo):
        self.__person_repo = person_repo
        self.__event_repo = event_repo

    def validate_registration(self, person_id, event_id):
        """
        Verifica daca ID-urile se afla in liste
        :param person_id: persoana inregistrata
        :param event_id: evenimentul la care este inregistrata persoana
        Exceptions: daca person sau event nu sunt de tipul Person sau Event
        """
        errors = []
        if not self.__person_repo.is_id_in_list(person_id):
            errors.append(f'Persoana cu ID-ul {person_id} nu se afla in lista')
        if not self.__event_repo.is_id_in_list(event_id):
            errors.append(f'Evenimentul cu ID-ul {event_id} nu se afla in lista')
        if errors:
            raise ValueError(', '.join(errors))
