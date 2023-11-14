from validators.person_validator import *


def test_person_validator():
    bob = Person(123, 'Marcel', 'Viteazu 20')
    validator = PersonValidator
    try:
        validator.validate_person(bob)
        assert True
    except ValueError:
        assert False

    try:
        bob.set_id('')
        validator.validate_person(bob)
        assert False
    except ValueError:
        assert True

    try:
        bob.set_name('')
        validator.validate_person(bob)
        assert False
    except ValueError:
        assert True

    try:
        bob.set_address('')
        validator.validate_person(bob)
        assert False
    except ValueError:
        assert True
