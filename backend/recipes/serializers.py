from rest_framework import serializers
from .models.Prescription import Prescription


class PrescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'