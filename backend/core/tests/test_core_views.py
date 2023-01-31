import json
import pytest
from django.urls import reverse
from historical.models.History import History


patientes_url = reverse("core_api:patientesviewset-list")
pytestmark = pytest.mark.django_db


def test_zero_patiente_should_return_empty_list(client) -> None:
    response = client.get(patientes_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_one_patiente_should_return_succeed(client, setupaciente) -> None:
    response = client.get(patientes_url)
    response.status_code == 200
    response_content = json.loads(response.content)[0]
    response_content['name'] == setupaciente[0].name
    response_content['cpf'] == setupaciente[0].cpf
    response_content['birth'] == setupaciente[0].birth
    response_content['cel'] == setupaciente[0].cel
    response_content['address'] == setupaciente[0].address
    response_content['profession'] == setupaciente[0].profession
    response_content['active'] == setupaciente[0].active
    response_content['gender'] == setupaciente[0].gender
