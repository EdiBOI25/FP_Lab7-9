from domain.person import Person


class PersonValidator:
    @staticmethod
    def validate_person(person: Person):
        """
        Valideaza datele unei persoane
        :param person: persoana
        Exceptions: daca datele sunt goale
        """
        errors = []
        if person.get_id() == '':
            errors.append('ID-ul nu poate fi gol')
        if person.get_name() == '':
            errors.append('Numele nu poate fi gol')
        if person.get_address() == '':
            errors.append('Adresa nu poate fi goala')
        if errors:
            raise ValueError(', '.join(errors))
