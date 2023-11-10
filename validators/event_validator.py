from domain.event import Event


def validate_event(event: Event):
    """
    Valideaza datele unui eveniment
    :param event: evenimentul
    Exceptions: daca datele sunt goale
    """
    errors = ''
    if event.get_id() == '':
        errors += 'ID-ul nu poate fi gol'
    if event.get_date() == '':
        errors += 'Data nu poate fi goala'
    if event.get_duration() == '':
        errors += 'Durata nu poate fi goala'
    if event.get_description() == '':
        errors += 'Descrierea nu poate fi goala'
    if len(errors) > 0:
        raise ValueError(errors)
