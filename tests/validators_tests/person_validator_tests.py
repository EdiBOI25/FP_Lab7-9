from validators.person_validator import *


def test_person_validator():
    bob = Person(123, 'Marcel', 'Viteazu 20')
    try:
        validate(bob)
        assert True
    except ValueError:
        assert False
    try:
        bob.set_id('')
        validate(bob)
        assert False
    except ValueError:
        assert True
    try:
        bob.set_name('')
        validate(bob)
        assert False
    except ValueError:
        assert True
    try:
        bob.set_address('')
        validate(bob)
        assert False
    except ValueError:
        assert True
