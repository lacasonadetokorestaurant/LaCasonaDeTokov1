from django import forms
from .models import Reserva


class ReservaMesaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = '__all__'
