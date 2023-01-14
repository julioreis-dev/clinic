from rest_framework import serializers
from .models import Patiente


class PatienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patiente
        fields = '__all__'