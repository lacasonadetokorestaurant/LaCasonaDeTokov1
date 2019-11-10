from django import forms
from .models import Reservacion
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import inlineformset_factory
User = get_user_model()

class ReservaForm(forms.ModelForm):

    class Meta: 
        model = Reservacion
        fields = 'nombre','email','telefono','cantidad_personas','hora_reserva','fecha','observacion'