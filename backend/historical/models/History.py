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


class History(Base):
    tabagism = models.BooleanField(verbose_name='Fumante', default=False)
    alcoholic = models.BooleanField(verbose_name='Uso de alcool', default=False)
    work_out = models.CharField(verbose_name='Pratica exercícios', max_length=150, blank=True)
    dst = models.CharField(verbose_name='Doença sexualmente transmissíveis', max_length=150, null=True, blank=True)
    illicit_substances = models.CharField(verbose_name='Substâncias Ilícitas', max_length=150, null=True, blank=True)
    familiar_history = models.TextField(verbose_name='Histórico Familiar', null=True, blank=True)
    old_medication = models.TextField(verbose_name='Medicação em uso', null=True, blank=True)
    conduct = models.TextField(verbose_name='Conduta', null=True, blank=True)
    patiente = models.ForeignKey(Patiente, null=True, blank=True, on_delete=models.CASCADE, related_name='history')

    class Meta:
        app_label = 'historical'
