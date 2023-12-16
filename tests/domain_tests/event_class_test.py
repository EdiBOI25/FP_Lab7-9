from domain.event import *


def test_event():
    untold = Event(1234, date(2020, 1, 5), time(1, 25), '2020\'s best festival!')
    assert untold.get_id() == 1234
    assert untold.get_date() == date(2020, 1, 5)
    assert untold.get_duration() == time(1, 25)
    assert untold.get_description() == '2020\'s best festival!'
    untold.set_id(1235)
    assert untold.get_id() == 1235
    untold.set_date(date(2021, 10, 3))
    assert untold.get_date() == date(2021, 10, 3)
    untold.set_duration(time(10, 15))
    assert untold.get_duration() == time(10, 15)
    untold.set_description('Worst event')
    assert untold.get_description() == 'Worst event'
