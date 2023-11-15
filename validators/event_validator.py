from domain.event import Event


class EventValidator:
    @staticmethod
    def validate_event(event: Event):
        """
        Valideaza datele unui eveniment
        :param event: evenimentul
        Exceptions: daca datele sunt goale
        """
        errors = []
        if event.get_id() == '':
            errors.append('ID-ul nu poate fi gol')
        if event.get_date() == '':
            errors.append('Data nu poate fi goala')
        if event.get_duration() == '':
            errors.append('Durata nu poate fi goala')
        if event.get_description() == '':
            errors.append('Descrierea nu poate fi goala')
        if errors:
            raise ValueError(', '.join(errors))
