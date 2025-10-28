from django.db import models


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
