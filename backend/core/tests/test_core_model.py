import pytest

pytestmark = pytest.mark.django_db


def test_patiente_info(setupaciente):
    assert setupaciente["set_a"].name == setupaciente["set_b"]['name']
    assert setupaciente["set_a"].cpf == setupaciente["set_b"]['cpf']
    assert setupaciente["set_a"].cel == setupaciente["set_b"]['cel']
    assert setupaciente["set_a"].birth == setupaciente["set_b"]['birth']
    assert setupaciente["set_a"].address == setupaciente["set_b"]['address']
    assert setupaciente["set_a"].profession == setupaciente["set_b"]['profession']
    assert setupaciente["set_a"].active == setupaciente["set_b"]['active']
    assert setupaciente["set_a"].gender == setupaciente["set_b"]['gender']
