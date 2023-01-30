from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PatientesViewSet

app_name = 'core_api'

router = DefaultRouter()
router.register('patientes', viewset=PatientesViewSet, basename='patientesviewset')

urlpatterns = [
    path('', include(router.urls)),
]

