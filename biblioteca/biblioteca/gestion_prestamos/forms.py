from datetime import date
from django import forms
from .models import Prestamo, EstadoPrestamo
from gestion_libros.models import Libro
from gestion_socios.models import Socio


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = [
            "numero_prestamo",
            "vencimiento_prestamo",
            "libro",
            "socio",
            "estado",
        ]
        labels = {
            "numero_prestamo": "Número de préstamo",
            "vencimiento_prestamo": "Vencimiento",
            "libro": "Libro",
            "socio": "Socio",
            "estado": "Estado",
        }
        help_texts = {
            "vencimiento_prestamo": "Fecha límite de devolución.",
        }
        widgets = {
            "numero_prestamo": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "vencimiento_prestamo": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "libro": forms.Select(attrs={"class": "form-select"}),
            "socio": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Solo socios activos en el combo
        self.fields["socio"].queryset = Socio.objects.filter(estado="activo").order_by("apellidos", "nombres")
        # Ordenar libros por título
        self.fields["libro"].queryset = Libro.objects.all().order_by("titulo")

    def clean_vencimiento_prestamo(self):
        vto = self.cleaned_data.get("vencimiento_prestamo")
        if vto and vto < date.today():
            raise forms.ValidationError("El vencimiento no puede ser anterior a hoy.")
        return vto

    def clean(self):
        """
        Valida disponibilidad: cantidad_ejemplares - préstamos activos > 0
        """
        cleaned = super().clean()
        libro = cleaned.get("libro")
        estado = cleaned.get("estado")  # si siempre es ACTIVO al crear, esto igual cubre cambios

        if libro and (estado == EstadoPrestamo.ACTIVO):
            # préstamos activos del libro
            activos = Prestamo.objects.filter(libro=libro, estado=EstadoPrestamo.ACTIVO).count()
            disponibles = libro.cantidad_ejemplares - activos
            if disponibles <= 0:
                raise forms.ValidationError(
                    f"No hay ejemplares disponibles de «{libro.titulo}». "
                    f"Prestados activos: {activos} / Copias: {libro.cantidad_ejemplares}."
                )
        return cleaned
