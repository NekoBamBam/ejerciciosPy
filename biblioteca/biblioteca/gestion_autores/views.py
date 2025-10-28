from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor


def index_autores(request):
    """Página principal del módulo de autores."""
    return render(request, "gestion_autores/index_autores.html")


def crear_autor(request):
    """Formulario para crear un nuevo autor."""
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion_autores:listar_autores")
    else:
        form = AutorForm()
    return render(request, "gestion_autores/crear_autor.html", {"form": form})


def listar_autores(request):
    """Listado de autores cargados."""
    autores = Autor.objects.all()
    return render(request, "gestion_autores/listar_autores.html", {"autores": autores})
