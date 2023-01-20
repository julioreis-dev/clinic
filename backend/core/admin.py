from django.contrib import admin
from .models.Patiente import Patiente


class PatienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'birth', 'profession', 'gender', 'cel', 'address', 'active')
    readonly_fields = ("created_at", "updated_at")

admin.site.register(Patiente, PatienteAdmin)
