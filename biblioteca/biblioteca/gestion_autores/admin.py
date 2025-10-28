from django.contrib import admin
from .models import Autor


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("apellidos", "nombres", "pais_nacimiento")
    search_fields = ("apellidos", "nombres", "pais_nacimiento")

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
