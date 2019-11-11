from django import forms
from .models import Reservacion
import datetime

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"

class ReservaForm(forms.ModelForm):

    class Meta: 
        model = Reservacion
        fields = 'nombre','email','telefono','cantidad_personas','hora_reserva','fecha','observacion'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fecha"].widget = DateInput()
        self.fields["hora_reserva"].widget = TimeInput()
