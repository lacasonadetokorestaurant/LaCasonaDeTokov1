from django.shortcuts import render
from .models import Nosotros, Contenido, Galeria, Plato, TipoPlato

# Create your views here.

# Views Home
def home(request):
    nosotros = Nosotros.objects.all()
    contenido = Contenido.objects.all()
    plato = Plato.objects.all()
    tipo_plato = TipoPlato.objects.all()
    galeria = Galeria.objects.all()

    context = {
        'nosotros': nosotros,
        'contenido': contenido,
        'plato': plato,
        'tipo_plato': tipo_plato,
        'galeria': galeria,
    }

    return render(request, 'home/index.html', context)
