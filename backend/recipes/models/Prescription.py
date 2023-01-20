from ..models import *
from core.models import Patiente


class Base(models.Model):
    """
    Abstract Class used in other classes
    """
    created_at = models.DateTimeField(verbose_name='Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Ultima atualização', auto_now=True)

    class Meta:
        """
        This class makes the class Base be abstract
        """
        abstract = True


class Prescription(Base):
    alegations = models.TextField(verbose_name='Queixa Principal', null=True, blank=True)
    medication = models.TextField(verbose_name='Medicação', null=True, blank=True)
    exams = models.TextField(verbose_name='Exames', null=True, blank=True)
    patiente = models.ForeignKey(Patiente, null=True, blank=True, on_delete=models.CASCADE, related_name='prescription')

    class Meta:
        app_label = 'recipes'
