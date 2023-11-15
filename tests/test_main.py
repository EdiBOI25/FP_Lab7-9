from tests.domain_tests import person_class_tests, event_class_tests
from tests.validators_tests import person_validator_tests, event_validator_tests
from tests.repo_tests import person_repo_tests, event_repo_tests
from tests.service_tests import person_service_test, event_service_test


def execute_all_tests():
    person_class_tests.test_person()
    event_class_tests.test_event()
    person_validator_tests.test_person_validator()
    event_validator_tests.test_event_validator()
    person_repo_tests.test_person_repo()
    event_repo_tests.test_event_repo()
    person_service_test.test_person_service()
    event_service_test.test_event_service()
    print('Tests passed!')
