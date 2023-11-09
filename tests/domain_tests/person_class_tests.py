from domain.person import *


def test_person():
    bob = Person('5041210080038', 'Bob', 'Mihai Viteazu 25')
    assert bob.get_id() == '5041210080038'
    assert bob.get_name() == 'Bob'
    assert bob.get_address() == 'Mihai Viteazu 25'
    bob.set_id('36476548')
    assert bob.get_id() == '36476548'
    bob.set_name('Marcel')
    assert bob.get_name() == 'Marcel'
    bob.set_address('Dristor 2')
    assert bob.get_address() == 'Dristor 2'
