import pytest
from faker import Faker
from model_mommy import mommy
from ..models import Patiente
from historical.models.History import History


@pytest.fixture(scope='function')
def setupaciente():
    faker = Faker()
    dict_faker = {'name': faker.name(),
                  'cpf': faker.random_int(11111111111, 99999999999),
                  'birth': faker.date_of_birth(),
                  'cel': faker.random_int(11111111111, 99999999999),
                  'address': faker.address(),
                  'profession': faker.job(),
                  'active': False,
                  'gender': faker.profile()['sex']}
    return Patiente.objects.create(name=dict_faker['name'],
                                   cpf=dict_faker['cpf'],
                                   birth=dict_faker['birth'],
                                   cel=dict_faker['cel'],
                                   address=dict_faker['address'],
                                   profession=dict_faker['profession'],
                                   active=dict_faker['active'],
                                   gender=dict_faker['gender']), dict_faker
