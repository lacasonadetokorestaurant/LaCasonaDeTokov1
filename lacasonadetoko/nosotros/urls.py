from django.urls import path
from . import views

app_name = 'nosotros'

urlpatterns = [
    path('', views.seccion_nosotros, name='nosotros'),
]
