from django.contrib.auth.models import User
from django.test import TestCase
from home.models import Plato, TipoPlato


class PlatoTest(TestCase):
    def setUp(self):

        tipolato1= TipoPlato.objects.create(nombre="PESCADO")
        tipolato2 = TipoPlato.objects.create(nombre="POLLO")
        Plato.objects.create(nombre="Albacora Frita", precio="8990", tipo_plato= tipolato1)
        Plato.objects.create(nombre="Pollo a lo Pobre", precio="5990", tipo_plato=tipolato2)

    def test_plato_nombre(self):
        plato = Plato.objects.get(nombre="Albacora Frita")
        self.assertEqual(plato.nombre, "Albacora Frita")
