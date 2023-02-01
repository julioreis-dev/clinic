from django.contrib import admin
from .models.Prescription import Prescription


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patiente', "updated_at")
    readonly_fields = ("created_at", "updated_at")


admin.site.register(Prescription, PrescriptionAdmin)
