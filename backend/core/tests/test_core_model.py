import pytest

pytestmark = pytest.mark.django_db


def test_patiente_info(setupaciente):
    assert setupaciente[0].name == setupaciente[1]['name']
    assert setupaciente[0].cpf == setupaciente[1]['cpf']
    assert setupaciente[0].cel == setupaciente[1]['cel']
    assert setupaciente[0].birth == setupaciente[1]['birth']
    assert setupaciente[0].address == setupaciente[1]['address']
    assert setupaciente[0].profession == setupaciente[1]['profession']
    assert setupaciente[0].active == setupaciente[1]['active']
    assert setupaciente[0].gender == setupaciente[1]['gender']
