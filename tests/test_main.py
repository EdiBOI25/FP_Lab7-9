from tests.domain_tests import person_class_test, event_class_test, registration_class_test
from tests.validators_tests import person_validator_test, event_validator_test
from tests.repo_tests import person_repo_test, event_repo_test, registration_repo_test
from tests.service_tests import person_service_test, event_service_test, registration_service_test
from tests.utils_tests import general_utils_test


def execute_all_tests():
    person_class_test.test_person()
    event_class_test.test_event()
    registration_class_test.test_registration()
    person_validator_test.test_person_validator()
    event_validator_test.test_event_validator()
    person_repo_test.test_person_repo()
    event_repo_test.test_event_repo()
    registration_repo_test.test_registration_repo()
    person_service_test.test_person_service()
    event_service_test.test_event_service()
    general_utils_test.test_generate_id()
    general_utils_test.test_sort_event_list_by_description()
    registration_service_test.test_registration_service()
    print('Tests passed!')
