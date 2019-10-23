from django.shortcuts import render
from .models import Carta

# Create your views here.


def carta(request):
    carta = Carta.objects.all()

    context = {
        'carta': carta,
    }
    return render(request, 'carta/hola.html', context)
