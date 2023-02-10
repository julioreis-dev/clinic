import pytest

pytestmark = pytest.mark.django_db


def test_history_info(sethistory):
    assert sethistory["db_data"].tabagism == sethistory["random_data"]['tabagism']
    assert sethistory["db_data"].alcoholic == sethistory["random_data"]['alcoholic']
    assert sethistory["db_data"].work_out == sethistory["random_data"]['work_out']
    assert sethistory["db_data"].dst == sethistory["random_data"]['dst']
    assert sethistory["db_data"].illicit_substances == sethistory["random_data"]['illicit_substances']
    assert sethistory["db_data"].familiar_history == sethistory["random_data"]['familiar_history']
    assert sethistory["db_data"].old_medication == sethistory["random_data"]['old_medication']
    assert sethistory["db_data"].conduct == sethistory["random_data"]['conduct']

