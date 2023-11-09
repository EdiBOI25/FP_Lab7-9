from domain.event import Event


def validate_event(event: Event):
    if event.get_id() == '':
        raise ValueError('Event ID cannot be empty.')
    if event.get_date() == '':
        raise ValueError('Event date cannot be empty.')
    if event.get_duration() == '':
        raise ValueError('Event duration cannot be empty.')
    if event.get_description() == '':
        raise ValueError('Event description cannot be empty.')
