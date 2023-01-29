from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PatientesViewSet

app_name = 'core_api'

router_core = DefaultRouter()
router_core.register('patientes', viewset=PatientesViewSet, basename='patientesviewset')

urlpatterns = [
    # path('', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
