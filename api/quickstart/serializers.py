from django.contrib.auth.models import User, Group
from home.models import Plato, TipoPlato, Galeria
from reservacion.models import Reservacion
from rest_framework import serializers
 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
 
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PlatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plato
        fields = ('nombre', 'precio', 'tipo_plato')

class TipoPlatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TipoPlato
        fields = ('__all__')

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galeria
        fields = ('titulo', 'imagen',)

class ReservacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservacion
        fields = ('__all__')