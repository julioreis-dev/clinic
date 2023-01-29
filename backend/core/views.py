from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Patiente
from .serializers import PatienteSerializers
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import action
from historical.serializers import HistorySerializers

class PatientesViewSet(viewsets.ReadOnlyModelViewSet):
    """
    All patientes in database
    """
    serializer_class = PatienteSerializers
    queryset = Patiente.objects.all()

    @action(detail=True, methods=['get'])
    def listhistory(self, request, pk=None):
        """
        History of a patiente
        """
        response = self.get_object()
        serializer = HistorySerializers(response.history, many=False)
        return Response(serializer.data)

#
#
#
#
# class PatienteViewSet(viewsets.ModelViewSet):
#     pass