import pytest
from ..models import Patiente


@pytest.fixture(scope='function')
def setupaciente():
    return Patiente.objects.create(name='will smith', cpf='09632222145', cel='21963256987', address='street view')
