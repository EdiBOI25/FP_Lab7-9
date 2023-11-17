from tests.test_main import execute_all_tests
from ui.ui_class import UI
# TODO: fa UI
# TODO 2: extinde service
# TODO 3: fa un "register" repo care sa contina o lista de perechi de genu (id_client, id_event) si sterge
#   lista de eventuri/persoane din clasele person/event
# TODO 4: refa testele astfel incat la erori sa faci assert err == 'Asta e eroarea', adauga comentarii la functii
# TODO 5: fa cerintele alealalte (rapoarte etc)


if __name__ == '__main__':
    execute_all_tests()
    UI().run()
