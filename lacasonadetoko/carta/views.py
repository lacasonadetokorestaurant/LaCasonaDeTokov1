from django.shortcuts import render
from .models import Plato, Categoria

# Create your views here.


def seccion_carta(request):
    plato = Plato.objects.all()
    categoria = Categoria.objects.all()

    context = {
        'plato': plato,
        'categoria' : categoria
    }
    return render(request, 'carta/carta.html', context)
