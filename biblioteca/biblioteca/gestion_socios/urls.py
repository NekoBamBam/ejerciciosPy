from django.urls import path
from .views import crear_socio, listar_socios, index_socios


app_name = "gestion_socios"

urlpatterns = [
    path("socios/index", index_socios, name="index_socios"),
    path("socios/crear", crear_socio, name="crear_socio"),
    path("socios/listar", listar_socios, name="listar_socios"),
]
