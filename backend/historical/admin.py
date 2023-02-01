from django.contrib import admin
from .models.History import History


class HistoryAdmin(admin.ModelAdmin):
    list_display = ('patiente',)
    readonly_fields = ("created_at", "updated_at")


admin.site.register(History, HistoryAdmin)




