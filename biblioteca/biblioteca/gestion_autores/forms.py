from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["apellidos", "nombres", "pais_nacimiento"]
        labels = {
            "apellidos": "Apellidos",
            "nombres": "Nombres",
            "pais_nacimiento": "País de nacimiento",
        }
        widgets = {
            "apellidos": forms.TextInput(attrs={"class": "form-control"}),
            "nombres": forms.TextInput(attrs={"class": "form-control"}),
            "pais_nacimiento": forms.TextInput(attrs={"class": "form-control"}),
        }
