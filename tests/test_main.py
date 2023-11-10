from tests.domain_tests import person_class_tests, event_class_tests
from tests.validators_tests import person_validator_tests


def execute_all_tests():
    person_class_tests.test_person()
    event_class_tests.test_event()
    person_validator_tests.test_person_validator()
    print('Tests passed!')
