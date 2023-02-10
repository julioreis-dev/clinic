import pytest

pytestmark = pytest.mark.django_db


def test_patiente_info(setupaciente):
    assert setupaciente["db_data"].name == setupaciente["random_data"]['name']
    assert setupaciente["db_data"].cpf == setupaciente["random_data"]['cpf']
    assert setupaciente["db_data"].cel == setupaciente["random_data"]['cel']
    assert setupaciente["db_data"].birth == setupaciente["random_data"]['birth']
    assert setupaciente["db_data"].address == setupaciente["random_data"]['address']
    assert setupaciente["db_data"].profession == setupaciente["random_data"]['profession']
    assert setupaciente["db_data"].active == setupaciente["random_data"]['active']
    assert setupaciente["db_data"].gender == setupaciente["random_data"]['gender']
