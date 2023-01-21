import pytest
from ..models.Prescription import Prescription
from faker import Faker


@pytest.fixture(scope='function')
def setprescrition() -> tuple:
    faker = Faker()
    dict_faker = {'alegations': faker.name(), 'medication': faker.text(), 'exams': faker.text()}
    return Prescription.objects.create(alegations=dict_faker['alegations'],
                                       medication=dict_faker['medication'],
                                       exams=dict_faker['exams']), dict_faker
