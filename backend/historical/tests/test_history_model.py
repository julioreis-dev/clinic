import pytest

pytestmark = pytest.mark.django_db


def test_history_info(sethistory):
    assert sethistory[0].tabagism == sethistory[1]['tabagism']
    assert sethistory[0].alcoholic == sethistory[1]['alcoholic']
    assert sethistory[0].work_out == sethistory[1]['work_out']
    assert sethistory[0].dst == sethistory[1]['dst']
    assert sethistory[0].illicit_substances == sethistory[1]['illicit_substances']
    assert sethistory[0].familiar_history == sethistory[1]['familiar_history']
    assert sethistory[0].old_medication == sethistory[1]['old_medication']
    assert sethistory[0].conduct == sethistory[1]['conduct']
