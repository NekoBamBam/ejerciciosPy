from django.contrib import admin
from .models import Prestamo


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ("numero_prestamo", "libro", "socio", "fecha_prestamo", "vencimiento_prestamo", "estado")
    list_filter = ("estado", "fecha_prestamo")
    search_fields = ("numero_prestamo", "libro__titulo", "socio__apellidos", "socio__nombres", "socio__documento")
