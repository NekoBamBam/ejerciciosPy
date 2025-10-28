from django.urls import path
from .views import crear_prestamo, listar_prestamos, index_prestamos


app_name = "gestion_prestamos"

urlpatterns = [
    path("prestamos/index", index_prestamos, name="index_prestamos"),
    path("prestamos/crear", crear_prestamo, name="crear_prestamo"),
    path("prestamos/listar", listar_prestamos, name="listar_prestamos"),
]
