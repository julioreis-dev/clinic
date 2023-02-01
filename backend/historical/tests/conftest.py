import pytest
from faker import Faker
from model_mommy import mommy
from ..models.History import History
# from core.models.Patiente import Patiente

@pytest.fixture(scope='function')
def sethistory() -> tuple:
    faker = Faker()
    dict_faker = {'tabagism': True,
                  'alcoholic': False,
                  'work_out': faker.text(),
                  'dst': faker.text(),
                  'illicit_substances': faker.text(),
                  'familiar_history': faker.text(),
                  'old_medication': faker.text(),
                  'conduct': faker.text()
                  }
    return History.objects.create(tabagism=dict_faker['tabagism'],
                                  alcoholic=dict_faker['alcoholic'],
                                  work_out=dict_faker['work_out'],
                                  dst=dict_faker['dst'],
                                  illicit_substances=dict_faker['illicit_substances'],
                                  familiar_history=dict_faker['familiar_history'],
                                  old_medication=dict_faker['old_medication'],
                                  conduct=dict_faker['conduct']), dict_faker


