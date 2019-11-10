from django.shortcuts import render
from .models import Nosotros, Contenido, Galeria, Plato, TipoPlato

# Create your views here.

# View Nosotros

def seccion_home(request):
    nosotros = Nosotros.objects.all()
    contenido = Contenido.objects.all()
    galeria = Galeria.objects.all()
    plato = Plato.objects.all()
    tipo_plato = TipoPlato.objects.all()

    context = {
        'nosotros': nosotros,
        'contenido': contenido,
        'plato': plato,
        'galeria': galeria,
        'tipo_plato': tipo_plato,
    }

    return render(request, 'home/index.html', context)

