from ..models import *


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
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=150)
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True, null=False, blank=False)
    birth = models.DateField(verbose_name='Nascimento')
    profession = models.CharField(verbose_name='Profissão', max_length=50, null=False, blank=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=SEXO_CHOICES, blank=False, null=False,
                              default='N')
    cel = models.CharField(verbose_name='Celular', blank=True, max_length=11)
    address = models.CharField(verbose_name='Endereço', blank=True, max_length=150)
    active = models.BooleanField(default=True)

    class Meta:
        app_label = 'core'
