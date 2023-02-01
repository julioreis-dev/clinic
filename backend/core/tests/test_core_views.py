import json
import pytest
from django.urls import reverse
from historical.models.History import History
from datetime import date
import datetime


patientes_url = reverse("core_api:patientesviewset-list")
pytestmark = pytest.mark.django_db


def test_zero_patiente_should_return_empty_list(client) -> None:
    response = client.get(patientes_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_added_one_patiente_should_return_succeed(client, setupaciente) -> None:
    response = client.get(patientes_url)
    response.status_code == 200
    response_content = json.loads(response.content)[0]
    assert len(json.loads(response.content)) == 1
    assert response_content['name'] == setupaciente['set_a'].name
    assert response_content['cpf'] == setupaciente['set_a'].cpf
    assert response_content['birth'] == setupaciente['set_a'].birth.strftime("%Y-%m-%d")
    assert response_content['cel'] == setupaciente['set_a'].cel
    assert response_content['address'] == setupaciente['set_a'].address
    assert response_content['profession'] == setupaciente['set_a'].profession
    assert response_content['active'] == setupaciente['set_a'].active
    assert response_content['gender'] == setupaciente['set_a'].gender


def test_one_patiente_should_return_succeed(client, setupaciente) -> None:
    detail_url = reverse("core_api:patientesviewset-detail", kwargs={'pk': setupaciente["set_a"].id})
    response = client.get(detail_url)
    response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content['name'] == setupaciente["set_a"].name
    assert response_content['cpf'] == setupaciente["set_a"].cpf
    assert response_content['birth'] == setupaciente["set_a"].birth.strftime("%Y-%m-%d")
    assert response_content['cel'] == setupaciente["set_a"].cel
    assert response_content['address'] == setupaciente["set_a"].address
    assert response_content['profession'] == setupaciente["set_a"].profession
    assert response_content['active'] == setupaciente["set_a"].active
    assert response_content['gender'] == setupaciente["set_a"].gender


def test_one_patiente_extra_actions_history_should_return_succeed(client, setinstance) -> None:
    historical_url = reverse("core_api:patientesviewset-detail", kwargs={"pk": setinstance.patiente.id})
    extra_action_url = "{path}historical/".format(path=historical_url)
    response = client.get(extra_action_url)
    response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content['tabagism'] == setinstance.tabagism
    assert response_content['alcoholic'] == setinstance.alcoholic
    assert response_content['work_out'] == setinstance.work_out
    assert response_content['dst'] == setinstance.dst
    assert response_content['illicit_substances'] == setinstance.illicit_substances
    assert response_content['familiar_history'] == setinstance.familiar_history
    assert response_content['old_medication'] == setinstance.old_medication
    assert response_content['conduct'] == setinstance.conduct
    assert response_content['patiente'] == setinstance.pk


def test_one_patiente_extra_actions_prescription_should_return_succeed(client, setprescription) -> None:
    prescription_url = reverse("core_api:patientesviewset-detail", kwargs={"pk": setprescription.patiente.id})
    extra_action_url = "{path}prescription/".format(path=prescription_url)
    response = client.get(extra_action_url)
    response.status_code == 200
    response_content = json.loads(response.content)[0]
    assert response_content['alegations'] == setprescription.alegations
    assert response_content['medication'] == setprescription.medication
    assert response_content['exams'] == setprescription.exams
    assert response_content['patiente'] == setprescription.pk