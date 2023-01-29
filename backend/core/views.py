from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Patiente
from .serializers import PatienteSerializers
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from historical.serializers import HistorySerializers
from recipes.serializers import PrescriptionSerializers

class PatientesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    All patientes in database
    """
    serializer_class = PatienteSerializers
    queryset = Patiente.objects.all()

    @action(detail=True, url_path='historical', methods=['get'])
    def listhistory(self, request, pk=None):
        """
        History of a patiente
        """
        response = self.get_object()
        serializer = HistorySerializers(response.history, many=False)
        return Response(serializer.data)

    @action(detail=True, url_path='prescription', methods=['get'])
    def listprescription(self, request, pk=None):
        """
        Historical of all prescription to the patiente
        """
        response = self.get_object()
        serializer = PrescriptionSerializers(response.prescription.all(), many=True)
        return Response(serializer.data)
