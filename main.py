from tests.test_main import execute_all_tests
from ui.ui_class import UI


if __name__ == '__main__':
    execute_all_tests()
    people_file = 'data/people.txt'
    events_file = 'data/events.txt'
    registrations_file = 'data/registrations.txt'
    UI(people_file, events_file, registrations_file).run()
