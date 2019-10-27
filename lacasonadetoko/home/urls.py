from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.seccion_nosotros, name='nosotros'),
    path('', views.seccion_carta, name='carta'),
    path('', views.seccion_galeria, name='galeria'),
]
