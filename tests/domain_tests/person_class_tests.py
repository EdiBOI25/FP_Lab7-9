from domain.person import Person


def test_person():
    bob = Person(1234, 'Bob', 'Mihai Viteazu 25')
    assert bob.get_id() == 1234
    assert bob.get_name() == 'Bob'
    assert bob.get_address() == 'Mihai Viteazu 25'
    bob.set_id(1235)
    assert bob.get_id() == 1235
    bob.set_name('Marcel')
    assert bob.get_name() == 'Marcel'
    bob.set_address('Dristor 2')
    assert bob.get_address() == 'Dristor 2'
