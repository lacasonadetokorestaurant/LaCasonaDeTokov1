from django.contrib import admin
from .models import Nosotros, Contenido, Galeria, Plato, TipoPlato

# Register your models here.
class ListaPlato(admin.ModelAdmin):
    list_display = ['nombre', 'precio','tipo_plato']
    list_filter = ('tipo_plato','precio')

class ListaContenido(admin.ModelAdmin):
    list_display = ['titulo', 'descripcion']

class ListaGaleria(admin.ModelAdmin):
    list_display = ['titulo', 'imagen']

admin.site.register(Nosotros)
admin.site.register(Contenido, ListaContenido)
admin.site.register(Galeria, ListaGaleria)
admin.site.register(Plato, ListaPlato)
admin.site.register(TipoPlato)
