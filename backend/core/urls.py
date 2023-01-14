from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatienteViewSet

app_name = 'core_api'

router = DefaultRouter()
router.register('patiente', viewset= PatienteViewSet, basename='patienteviewset')

urlpatterns = [
    path('', include(router.urls)),
]
