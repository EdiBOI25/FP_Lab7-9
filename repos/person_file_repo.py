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
        try:
            file = open(self.__file_name, 'r')
        except IOError as e:
            print(e)
            return []
        line = file.readline().strip()
        result = []
        while line != '':
            params = line.split(',')
            person = Person(int(params[0]), params[1], params[2])
            print(person)
            result.append(person)
            line = file.readline().strip()
        file.close()
        return result
