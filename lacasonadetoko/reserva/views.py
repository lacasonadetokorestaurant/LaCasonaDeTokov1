from django.shortcuts import render
from .models import Reserva
from .forms import ReservaMesaForm

# Create your views here.


def reserva_mesa(request):
    reserva_form = ReservaMesaForm()

    if request.method == 'POST':
        reserva_form = ReservaMesaForm(request.POST)

        if reserva_form.is_valid():
           reserva_form.save()

    context = {'form': reserva_form}
    return render(request, 'reservation/reservation.html', context)
