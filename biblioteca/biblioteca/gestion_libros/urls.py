from django.urls import path
from .views import crear_libro, listar_libros, index_libros


app_name = "gestion_libros"

urlpatterns = [
    path("libros/index", index_libros, name="index_libros"),
    path("libros/crear", crear_libro, name="crear_libro"),
    path("libros/listar", listar_libros, name="listar_libros"),
]
