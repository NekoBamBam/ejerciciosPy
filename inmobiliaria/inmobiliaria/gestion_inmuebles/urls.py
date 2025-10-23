from django.urls import path
from .views import tarea

urlpatterns = [
    path("inmuebles/tarea",tarea, name="tarea"),
]
