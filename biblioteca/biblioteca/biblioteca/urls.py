"""
URL configuration for biblioteca project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("libros/", include(("gestion_libros.urls", "gestion_libros"), namespace="gestion_libros")),
    path("prestamos/", include(("gestion_prestamos.urls", "gestion_prestamos"), namespace="gestion_prestamos")),
    path("socios/", include(("gestion_socios.urls", "gestion_socios"), namespace="gestion_socios")),
    path("autores/", include(("gestion_autores.urls", "gestion_autores"), namespace="gestion_autores")),
]
