from django.urls import path
from . import views

app_name = 'carrusel'

urlpatterns = [
    path('', views.seccion_carrusel, name='carrusel'),

]
