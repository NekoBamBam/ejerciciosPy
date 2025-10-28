from django.contrib import admin
from .models import Autor, Libro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ("apellidos", "nombres", "pais_nacimiento")
    search_fields = ("apellidos", "nombres")

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "anio", "isbn", "cantidad_ejemplares", "estado")
    list_filter = ("estado", "anio", "idioma")
    search_fields = ("titulo", "autor__apellidos", "autor__nombres", "isbn")
