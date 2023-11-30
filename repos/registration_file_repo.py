from domain.registration import Registration


class RegistrationFileRepository:
    def __init__(self, file_name):
        self.__file_name = file_name

    def load_from_file(self):
        """
        Ia datele inscrierilor din fisier
        :return: lista de inscrieri
        """
        with open(self.__file_name, 'r') as file:
            line = file.readline().strip()
            result = []
            while line != '':
                params = line.split(',')
                registration = Registration(int(params[0]), int(params[1]))
                result.append(registration)
                line = file.readline().strip()
        return result

    def store_to_file(self, reg_list):
        """
        Stocheaza lista transmisa in fisier
        :param reg_list:
        :return:
        """
        with open(self.__file_name, 'w') as file:
            for reg in reg_list:
                str_reg = str(reg.get_person()) + ',' + str(reg.get_event()) + '\n'
                file.write(str_reg)
