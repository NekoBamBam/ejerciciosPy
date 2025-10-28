from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SocioForm


def index_socios(request):
    return render(request, "gestion_socios/index_socios.html")


def crear_socio(request):
    if request.method == "POST":
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            messages.success(request, f"Socio «{socio}» creado correctamente.")
            return redirect("gestion_socios:listar_socios")  # ajustá si tu lista tiene otro name
    else:
        form = SocioForm()
    return render(request, "gestion_socios/crear_socio.html", {"form": form})


def listar_socios(request):
    return render(request, "gestion_socios/listar_socios.html")
