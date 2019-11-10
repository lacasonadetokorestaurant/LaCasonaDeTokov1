from django.urls import path
from . import views

app_name = 'reservacion'

urlpatterns = [
    path('', views.reserva_mesa, name='reserva_mesa'),
]