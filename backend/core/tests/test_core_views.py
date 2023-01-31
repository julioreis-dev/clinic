import json
import pytest
from django.urls import reverse
from historical.models.History import History
from datetime import date


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
    assert len(json.loads(response.content)) == 1
    assert response_content['name'] == setupaciente[0].name
    assert response_content['cpf'] == str(setupaciente[0].cpf)
    # assert str(response_content['birth']) == str(f"{setupaciente[0].birth.year}-{setupaciente[0].birth.month}-{setupaciente[0].birth.day}")
    assert response_content['cel'] == str(setupaciente[0].cel)
    assert response_content['address'] == setupaciente[0].address
    assert response_content['profession'] == setupaciente[0].profession
    assert response_content['active'] == setupaciente[0].active
    assert response_content['gender'] == setupaciente[0].gender


def test_one_specifique_patiente_should_return_succeed(client, setupaciente) -> None:
    detail_url = reverse("core_api:patientesviewset-detail", kwargs={'pk': setupaciente[0].id})
    response = client.get(detail_url)
    response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content['name'] == setupaciente[0].name
    assert response_content['cpf'] == str(setupaciente[0].cpf)
    # assert response_content['birth'] == setupaciente[0].birth
    assert response_content['cel'] == str(setupaciente[0].cel)
    assert response_content['address'] == setupaciente[0].address
    assert response_content['profession'] == setupaciente[0].profession
    assert response_content['active'] == setupaciente[0].active
    assert response_content['gender'] == setupaciente[0].gender
