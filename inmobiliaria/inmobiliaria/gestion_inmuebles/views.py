from django.shortcuts import render

# Create your views here.
def tarea(request):
    return render(request, 'gestion_inmuebles/tarea.html')