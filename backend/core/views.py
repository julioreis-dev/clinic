from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Patiente
from .serializers import PatienteSerializers
from rest_framework.response import Response


class PatienteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PatienteSerializers
    queryset = Patiente.objects.all()