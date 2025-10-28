from datetime import date
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Libro, Autor


CURRENT_YEAR = date.today().year


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            "titulo", "autor", "idioma", "editorial", "edicion",
            "anio", "isbn", "cantidad_ejemplares", "estado",
        ]
        labels = {
            "titulo": "Título",
            "autor": "Autor",
            "idioma": "Idioma",
            "editorial": "Editorial",
            "edicion": "Edición",
            "anio": "Año de publicación",
            "isbn": "ISBN",
            "cantidad_ejemplares": "Cantidad de ejemplares",
            "estado": "Estado",
        }
        help_texts = {
            "anio": "Entre 1400 y el año actual.",
            "cantidad_ejemplares": "Número total de copias en la biblioteca.",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "autor": forms.Select(attrs={"class": "form-select"}),
            "idioma": forms.TextInput(attrs={"class": "form-control"}),
            "editorial": forms.TextInput(attrs={"class": "form-control"}),
            "edicion": forms.TextInput(attrs={"class": "form-control"}),
            "anio": forms.NumberInput(attrs={"class": "form-control", "min": 1400, "max": CURRENT_YEAR}),
            "isbn": forms.TextInput(attrs={"class": "form-control"}),
            "cantidad_ejemplares": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_anio(self):
        anio = self.cleaned_data.get("anio")
        if anio and (anio < 1400 or anio > CURRENT_YEAR):
            raise forms.ValidationError(f"El año debe estar entre 1400 y {CURRENT_YEAR}.")
        return anio
