from django.contrib import admin
from .models import Reservacion

# Register your models here.


class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'telefono','cantidad_personas', 'hora_reserva', 'fecha', 'estado']
    list_filter = ('nombre', 'fecha', 'estado', 'cantidad_personas')


admin.site.register(Reservacion, Lista)
