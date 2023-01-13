import pytest


pytestmark = pytest.mark.django_db


def test_patiente_info(setupaciente):
    assert setupaciente.name == 'will smith'
    assert setupaciente.cpf == '09632222145'
    assert setupaciente.cel == '21963256987'
    assert setupaciente.birth =='2023-02-18'
    assert setupaciente.address == 'street view'

