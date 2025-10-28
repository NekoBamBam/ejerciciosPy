from django.db import models


class EstadoSocio(models.TextChoices):
    ACTIVO = "activo", "Activo"
    SUSPENDIDO = "suspendido", "Suspendido"
    BAJA = "baja", "Baja"


class Socio(models.Model):
    numero_socio = models.PositiveIntegerField(unique=True)
    apellidos = models.CharField(max_length=120)
    nombres = models.CharField(max_length=120)
    direccion = models.CharField(max_length=200, blank=True)
    documento = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estado = models.CharField(
        max_length=20,
        choices=EstadoSocio.choices,
        default=EstadoSocio.ACTIVO
    )

    class Meta:
        ordering = ["apellidos", "nombres"]
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return f"{self.apellidos}, {self.nombres} (N° {self.numero_socio})"
