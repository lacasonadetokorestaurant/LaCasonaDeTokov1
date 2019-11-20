from django.contrib.auth.models import User
from django.test import TestCase


class UsuarioTest(TestCase):
    def setUp(self):
        self.usuario1 = {
            'username': 'testusuario',
            'first_name': 'test',
            'last_name': 'usuario',
            'email': 'testusuario@gmail.com',
            'password': 'testusuario1234'}
        User.objects.create_user(**self.usuario1)

        self.usuario2 = {
            'username': 'testusuario2',
            'first_name': 'test2',
            'last_name': 'usuario2',
            'email': 'testusuario2@gmail.com',
            'password': 'testusuario21234'}
        User.objects.create_user(**self.usuario2)

    def test_usuario_username(self):
        usuario = User.objects.get(username="testusuario")
        self.assertEqual(usuario.username, "testusuario")
