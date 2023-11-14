from domain.event import Event


def generate_id(event_list):
    """
    Genereaza un ID nou
    :param event_list: lista de persoane
    :return:
    """
    result_id = 0
    for event in event_list:
        result_id = max(result_id, event.get_id())
    return result_id + 1
