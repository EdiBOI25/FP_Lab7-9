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


def sort_event_list_by_description(this_list):
    for elem in this_list:
        if not isinstance(elem, Event):
            raise TypeError('Cel putin un element in lista nu este de tipul Eveniment.')
    # return sorted(this_list, key=lambda ev: ev.get_description())
    this_list.sort(key=lambda ev: ev.get_description())
    return this_list


def sort_event_list_by_date(this_list):
    for elem in this_list:
        if not isinstance(elem, Event):
            raise TypeError('Cel putin un element in lista nu este de tipul Eveniment.')
    # return sorted(this_list, key=lambda ev: ev.get_description())
    this_list.sort(key=lambda ev: ev.get_date())
    return this_list


def bubble_sort(lst, key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
    if reverse == True:
        cmp = lambda x, y: x > y
    result = list(lst)
    done = False
    while not done:
        done = True
        for i in range(len(result) - 1):
            if cmp(key(result[i + 1]), key(result[i])):
                result[i], result[i + 1] = result[i + 1], result[i]
                done = False
    return result


def shell_sort(lst, key=lambda x: x, reverse=False, cmp=lambda x, y: x < y):
    if reverse == True:
        cmp = lambda x, y: x > y
    result = list(lst)
    length = len(result)
    interval = length // 2
    while interval > 0:
        for i in range(interval, length):
            temp = result[i]
            j = i
            # while j >= interval and result[j - interval] > temp:
            while j >= interval and not cmp(key(result[j - interval]), key(temp)):
                result[j] = result[j - interval]
                j -= interval
            result[j] = temp
        interval //= 2
    return result
