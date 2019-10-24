from django.urls import path
from . import views

app_name = 'carta'

urlpatterns = [
    path('', views.seccion_carta, name='carta'),
]
