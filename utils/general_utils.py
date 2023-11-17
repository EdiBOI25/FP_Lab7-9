from domain.event import Event
from domain.person import Person


def generate_id(this_list):
    """
    Genereaza un ID nou
    :param this_list: lista de chestii care au id
    :return: nout id generat
    """
    if not this_list:
        return 1
    for elem in this_list:
        if not isinstance(elem, Event) and not isinstance(elem, Person):
            raise TypeError('Cel putin un element in lista nu este de tipul Persoana sau Eveniment.')

    result_id = 0
    for elem in this_list:
        result_id = max(result_id, elem.get_id())
    return result_id + 1
