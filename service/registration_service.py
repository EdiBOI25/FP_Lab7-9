from repos.registration_repo import RegistrationRepo


class RegistrationService:
    def __init__(self):
        self.__repo = RegistrationRepo()

    def get_all(self):
        return self.__repo.get_all()

    def __str__(self):
        return str(self.__repo)

    def add_registration(self, person_id, event_id):
        self.__repo.add_registration(person_id, event_id)

    def remove_registration(self, person_id, event_id):
        self.__repo.remove_registration(person_id, event_id)

    def get_events_of_person(self, person_id):
        return self.__repo.get_events_of_person(person_id)

    def get_persons_of_event(self, event_id):
        return self.__repo.get_persons_of_event(event_id)
