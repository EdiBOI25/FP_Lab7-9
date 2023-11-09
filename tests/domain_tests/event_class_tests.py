from domain.event import *


def test_event():
    untold = Event('8493938473', '01-08-2020', '1h 25min', '2020\'s best festival!')
    assert untold.get_id() == '8493938473'
    assert untold.get_date() == '01-08-2020'
    assert untold.get_duration() == '1h 25min'
    assert untold.get_description() == '2020\'s best festival!'
    untold.set_id('1212')
    assert untold.get_id() == '1212'
    untold.set_date('03-11-2021')
    assert untold.get_date() == '03-11-2021'
    untold.set_duration('2h 30min')
    assert untold.get_duration() == '2h 30min'
    untold.set_description('Worst event')
    assert untold.get_description() == 'Worst event'
