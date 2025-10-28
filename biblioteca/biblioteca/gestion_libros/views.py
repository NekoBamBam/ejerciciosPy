from django.shortcuts import render, redirect
from .forms import LibroForm


def index_libros(request):
    return render(request, "gestion_libros/index_libros.html")


def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gestion_libros:listar_libros")
    else:
        form = LibroForm()
    return render(request, "gestion_libros/crear_libro.html", {"form": form})


def listar_libros(request):
    return render(request, "gestion_libros/listar_libros.html")
