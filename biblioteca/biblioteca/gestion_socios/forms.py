from django import forms
from .models import Socio, EstadoSocio


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = [
            "numero_socio", "apellidos", "nombres", "direccion",
            "documento", "fecha_nacimiento", "estado",
        ]
        labels = {
            "numero_socio": "Número de socio",
            "apellidos": "Apellidos",
            "nombres": "Nombres",
            "direccion": "Dirección",
            "documento": "Documento",
            "fecha_nacimiento": "Fecha de nacimiento",
            "estado": "Estado",
        }
        widgets = {
            "numero_socio": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "nombres": forms.TextInput(attrs={"class": "form-control"}),
            "direccion": forms.TextInput(attrs={"class": "form-control"}),
            "documento": forms.TextInput(attrs={"class": "form-control"}),
            "fecha_nacimiento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }
