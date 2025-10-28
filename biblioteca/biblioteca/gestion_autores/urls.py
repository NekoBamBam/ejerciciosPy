from django.urls import path
from .views import crear_autor, listar_autores, index_autores


app_name = "gestion_autores"

urlpatterns = [
    path("autores/index", index_autores, name="index_autores"),
    path("autores/crear", crear_autor, name="crear_autor"),
    path("autores/listar", listar_autores, name="listar_autores"),
]
