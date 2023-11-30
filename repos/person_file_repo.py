from validators.person_validator import *


class PersonFileRepository:
    def __init__(self, file_name):
        self.__validator = PersonValidator()
        self.__file_name = file_name

    def load_from_file(self):
        """
        Ia datele persoanelor din fisier
        :return: lista de persoane
        """
        with open(self.__file_name, 'r') as file:
            line = file.readline().strip()
            result = []
            while line != '':
                params = line.split(',')
                person = Person(int(params[0]), params[1], params[2])
                result.append(person)
                line = file.readline().strip()
        return result

    def store_to_file(self, per_list):
        """
        Stocheaza lista transmisa in fisier
        :param per_list:
        :return:
        """
        with open(self.__file_name, 'w') as file:
            for per in per_list:
                str_per = str(per.get_id()) + ',' + per.get_name() + ',' + per.get_address() + '\n'
                file.write(str_per)
