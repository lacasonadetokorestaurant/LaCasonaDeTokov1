from django.shortcuts import render
from .models import Nosotros, Contenido, Galeria, Plato, TipoPlato

# Create your views here.

# View Nosotros


def seccion_nosotros(request):
    nosotros = Nosotros.objects.all()
    contenido = Contenido.objects.all()

    context = {
        'nosotros': nosotros,
        'contenido': contenido
    }

    return render(request, 'home/index.html', context)


# View Carta
def seccion_carta(request):
    plato = Plato.objects.all()
    tipo_plato = TipoPlato.objects.all()

    context = {
        'plato': plato,
        'tipo_plato': tipo_plato
    }
    return render(request, 'home/index.html', context)

# Views Galeria
def seccion_galeria(request):
    galeria = Galeria.objects.all()

    context = {
        'galeria': galeria,
    }
    return render(request, 'home/index.html', context)
