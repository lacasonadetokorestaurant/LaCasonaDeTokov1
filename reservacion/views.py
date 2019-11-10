from django.shortcuts import render
from reservacion.models import Reservacion
from .forms import ReservaForm
from django.http import HttpResponse,HttpResponseRedirect

def reserva_mesa(request):
    reserva_form = ReservaForm()

    if request.method == 'POST':
        reserva_form = ReservaForm(request.POST)

        if reserva_form.is_valid():
            reserva_form = reserva_form.save(commit=False)
            reserva_form.save()
        else:
            reserva_form = ReservaForm()

    context = {'form': reserva_form}
    
    return render(request, 'reserva.html',context)