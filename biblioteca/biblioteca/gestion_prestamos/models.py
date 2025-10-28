from django.db import models
from django.core.validators import MinValueValidator


class EstadoPrestamo(models.TextChoices):
    ACTIVO = "activo", "Activo"
    DEVUELTO = "devuelto", "Devuelto"
    VENCIDO = "vencido", "Vencido"


class Prestamo(models.Model):
    numero_prestamo = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])
    fecha_prestamo = models.DateField(auto_now_add=True)
    vencimiento_prestamo = models.DateField()

    # Referencias perezosas por string para evitar importación circular
    libro = models.ForeignKey("gestion_libros.Libro", on_delete=models.PROTECT, related_name="prestamos")
    socio = models.ForeignKey("gestion_socios.Socio", on_delete=models.PROTECT, related_name="prestamos")

    estado = models.CharField(
        max_length=20,
        choices=EstadoPrestamo.choices,
        default=EstadoPrestamo.ACTIVO
    )

    class Meta:
        ordering = ["-fecha_prestamo"]
        verbose_name = "Préstamo"
        verbose_name_plural = "Préstamos"

    def __str__(self):
        return f"Préstamo #{self.numero_prestamo} - {self.libro} → {self.socio} [{self.estado}]"
