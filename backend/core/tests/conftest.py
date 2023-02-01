import pytest
from faker import Faker
from model_mommy import mommy
from ..models import Patiente
from historical.models.History import History
from recipes.models.Prescription import Prescription


@pytest.fixture(scope='function')
def setupaciente():
    faker = Faker()
    dict_faker = {'name': faker.name(),
                  'cpf': str(faker.random_int(11111111111, 99999999999)),
                  'birth': faker.date_of_birth(),
                  'cel': str(faker.random_int(11111111111, 99999999999)),
                  'address': faker.address(),
                  'profession': faker.job(),
                  'active': False,
                  'gender': faker.profile()['sex']}
    return {"set_a":Patiente.objects.create(name=dict_faker['name'],
                                   cpf=dict_faker['cpf'],
                                   birth=dict_faker['birth'],
                                   cel=dict_faker['cel'],
                                   address=dict_faker['address'],
                                   profession=dict_faker['profession'],
                                   active=dict_faker['active'],
                                   gender=dict_faker['gender']),
            "set_b":dict_faker}

@pytest.fixture(scope='function')
def setinstance():
    patiente = mommy.make(Patiente)
    faker = Faker()
    return History.objects.create(tabagism= True,
                                  alcoholic= False,
                                  work_out= faker.text(),
                                  dst= faker.text(),
                                  illicit_substances= faker.text(),
                                  familiar_history= faker.text(),
                                  old_medication= faker.text(),
                                  conduct= faker.text(),
                                  patiente=patiente)


@pytest.fixture(scope='function')
def setprescription():
    patiente = mommy.make(Patiente)
    faker = Faker()
    return Prescription.objects.create(alegations= faker.text(),
                                       medication= faker.text(),
                                       exams= faker.text(),
                                       patiente=patiente)
