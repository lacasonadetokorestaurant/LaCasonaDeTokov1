from django.shortcuts import render
from .models import Carrusel

# Create your views here.


def seccion_carrusel(request):
    carrusel = Carrusel.objects.all()

    context = {
        'carrusel': carrusel
    }

    return  render(request, 'carrusel/carrusel.html', context)
