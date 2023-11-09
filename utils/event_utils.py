from domain.event import Event


def add_event(event_list, event: Event):
    if event in event_list:
        print(f'Evenimentul se afla deja in lista.')
        return
    event_list.append(event)


def remove_event(event_list, event: Event):
    if event not in event_list:
        print(f'Evenimentul nu a fost gasit in lista.')
        return
    event_list.remove(event)


def search_event_by_id(event_list, idcode) -> Event:
    for event in event_list:
        if event.get_id() == idcode:
            return event
