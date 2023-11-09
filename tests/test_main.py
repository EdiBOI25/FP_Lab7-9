from tests.domain_tests import person_class_tests, event_class_tests


def execute_all_tests():
    person_class_tests.test_person()
    event_class_tests.test_event()
    print('Tests passed!')
