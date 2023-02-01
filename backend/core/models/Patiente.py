from ..models import *
# from historical.models import History


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


class Patiente(Base):
    GENDER_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )

    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=150)
    cpf = models.CharField(verbose_name='CPF', max_length=11, unique=True, null=False, blank=False)
    birth = models.DateField(verbose_name='Nascimento')
    profession = models.CharField(verbose_name='Profissão', max_length=50, null=False, blank=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=GENDER_CHOICES, blank=False, null=False,
                              default='N')
    cel = models.CharField(verbose_name='Celular', blank=True, max_length=11)
    address = models.CharField(verbose_name='Endereço', blank=True, max_length=150)
    active = models.BooleanField(default=True)
    # history = models.OneToOneField(History, null=True, blank=True, on_delete=models.CASCADE, related_name='patiente')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Patiente'
        verbose_name_plural = 'Patientes'
        app_label = 'core'
