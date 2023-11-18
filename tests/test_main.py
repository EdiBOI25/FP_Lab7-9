from tests.domain_tests import person_class_tests, event_class_tests, registration_class_test
from tests.validators_tests import person_validator_tests, event_validator_tests
from tests.repo_tests import person_repo_tests, event_repo_tests, registration_repo_tests
from tests.service_tests import person_service_test, event_service_test, registration_service_test
from tests.utils_tests import general_utils_test


def execute_all_tests():
    person_class_tests.test_person()
    event_class_tests.test_event()
    registration_class_test.test_registration()
    person_validator_tests.test_person_validator()
    event_validator_tests.test_event_validator()
    person_repo_tests.test_person_repo()
    event_repo_tests.test_event_repo()
    registration_repo_tests.test_registration_repo()
    person_service_test.test_person_service()
    event_service_test.test_event_service()
    general_utils_test.test_generate_id()
    registration_service_test.test_registration_service()
    print('Tests passed!')
