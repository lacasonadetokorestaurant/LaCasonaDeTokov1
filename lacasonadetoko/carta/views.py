from django.shortcuts import render
from .models import Carta, Categoria

# Create your views here.


def seccion_carta(request):
    carta = Carta.objects.all()
    categoria = Categoria.objects.all()

    context = {
        'carta' : carta,
        'categoria' : categoria
    }
    return render(request, 'carta/carta.html', context)
