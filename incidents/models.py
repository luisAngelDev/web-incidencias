from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Incident(models.Model):
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    reportado_por = models.CharField(max_length=100)
    tipo_incidente = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    prioridad = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=30, blank=True)
    responsable = models.CharField(max_length=30, blank=True)
    fecha_solucion = models.DateTimeField(null=True, blank=True)
    acciones_realizadas = models.TextField(blank=True)
    resultado = models.CharField(max_length=100, blank=True) 
    revisado_por = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_incidente + ' - by ' + self.user.username