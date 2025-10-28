from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date

CURRENT_YEAR = date.today().year


class Autor(models.Model):
    apellidos = models.CharField(max_length=120)
    nombres = models.CharField(max_length=120)
    pais_nacimiento = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ["apellidos", "nombres"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.apellidos}, {self.nombres}"


class EstadoLibro(models.TextChoices):
    DISPONIBLE = "disponible", "Disponible"
    PRESTADO = "prestado", "Prestado"
    BAJA = "baja", "Baja"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT, related_name="libros")
    idioma = models.CharField(max_length=60, blank=True)
    editorial = models.CharField(max_length=120, blank=True)
    edicion = models.CharField(max_length=50, blank=True)
    anio = models.PositiveIntegerField(
        validators=[MinValueValidator(1400), MaxValueValidator(CURRENT_YEAR)],
        help_text="Año de publicación"
    )
    isbn = models.CharField(max_length=20, unique=True)
    cantidad_ejemplares = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        help_text="Cantidad de copias del libro en la biblioteca"
    )
    estado = models.CharField(
        max_length=20,
        choices=EstadoLibro.choices,
        default=EstadoLibro.DISPONIBLE
    )

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"

    def __str__(self):
        return f"{self.titulo} ({self.anio}) — {self.autor}"
