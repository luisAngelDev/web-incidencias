from django.contrib import admin
from .models import Incident

class IncidentAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_reporte", )


# Register your models here.

admin.site.register(Incident, IncidentAdmin)