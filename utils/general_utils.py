def generate_id(this_list):
    """
    Genereaza un ID nou
    :param this_list: lista de chestii care au id
    :return: nout id generat
    """
    result_id = 0
    for elem in this_list:
        result_id = max(result_id, elem.get_id())
    return result_id + 1
