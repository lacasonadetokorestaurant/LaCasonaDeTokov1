from django.shortcuts import render
from .models import Galeria

# Create your views here.


def seccion_galeria(request):
    galeria = Galeria.objects.all()
    

    context = {
        'galeria': galeria,
    }
    return render(request, 'galeria/galeria.html', context)

# Create your views here.
