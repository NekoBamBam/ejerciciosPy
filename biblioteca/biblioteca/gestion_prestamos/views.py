from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PrestamoForm


def index_prestamos(request):
    return render(request, "gestion_prestamos/index_prestamos.html")


def crear_prestamo(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save()
            messages.success(request, f"Préstamo #{prestamo.numero_prestamo} creado correctamente.")
            return redirect("gestion_prestamos:listar_prestamos") 
    else:
        form = PrestamoForm()
    return render(request, "gestion_prestamos/crear_prestamo.html", {"form": form})


def listar_prestamos(request):
    return render(request, "gestion_prestamos/listar_prestamos.html")
