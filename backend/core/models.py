from django.db import models


class Base(models.Model):
    """
    Abstract Class used in other classes
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        This class makes the class Base be abstract
        """
        abstract = True


class Patiente(Base):
    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=150)
    cpf = models.CharField(verbose_name='CPF')
    birth = models.DateField(verbose_name='Nascimento')
    cel = models.CharField(verbose_name='Celular', blank=True, max_length=150)
    address = models.CharField(verbose_name='Endereço', blank=True, max_length=150)
    active = models.BooleanField(default=True)
