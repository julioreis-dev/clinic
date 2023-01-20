from django.contrib import admin
from .models.Prescription import Prescription


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('alegations', 'medication', 'exams', 'created_at', 'updated_at', 'patiente')
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Prescription, PrescriptionAdmin)
