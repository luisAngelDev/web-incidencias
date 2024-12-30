from django import forms
from .models import Incident

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['reportado_por', 'tipo_incidente', 'descripcion', 'prioridad', 'estado', 'responsable', 'acciones_realizadas', 'resultado', 'revisado_por', ]
        widgets = {
            'reportado_por': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_incidente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'prioridad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'responsable': forms.TextInput(attrs={'class': 'form-control'}),
            'acciones_realizadas': forms.Textarea(attrs={'class': 'form-control'}),
            'resultado': forms.TextInput(attrs={'class': 'form-control'}),
            'revisado_por': forms.TextInput(attrs={'class': 'form-control'}),
        }