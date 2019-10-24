from django.shortcuts import render
from .models import Contenido, Nosotros

# Create your views here.


def seccion_nosotros(request):
    nosotros = Nosotros.objects.all()
    contenido = Contenido.objects.all()

    context = {
        'nosotros': nosotros,
        'contenido': contenido
    }

    return render(request, 'nosotros/nosotros.html', context)
