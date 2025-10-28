from django.contrib import admin
from .models import Socio


@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ("numero_socio", "apellidos", "nombres", "documento", "estado")
    list_filter = ("estado",)
    search_fields = ("apellidos", "nombres", "documento", "numero_socio")

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"
