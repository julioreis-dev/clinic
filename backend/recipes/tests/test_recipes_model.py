import pytest

pytestmark = pytest.mark.django_db


def test_prescrition_info(setprescrition):
    assert setprescrition[0].alegations == setprescrition[1]['alegations']
    assert setprescrition[0].medication == setprescrition[1]['medication']
    assert setprescrition[0].exams == setprescrition[1]['exams']
