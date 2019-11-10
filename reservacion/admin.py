from django.contrib import admin
from .models import Reservacion

# Register your models here.

class Lista(admin.ModelAdmin):
    list_display = ['nombre', 'cantidad_personas','fecha','estado']
    list_filter = ('fecha','estado','cantidad_personas')


admin.site.register(Reservacion, Lista)
