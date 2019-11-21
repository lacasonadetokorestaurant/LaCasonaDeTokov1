from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from home.models import Plato, TipoPlato, Galeria
from reservacion.models import Reservacion
from api.quickstart.serializers import UserSerializer, GroupSerializer, PlatoSerializer, TipoPlatoSerializer, GaleriaSerializer, ReservacionSerializer 
 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
 
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plato to be viewed or edited.
    """
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class TipoPlatoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tipoplato to be viewed or edited.
    """
    queryset = TipoPlato.objects.all()
    serializer_class = TipoPlatoSerializer

class GaleriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows galeria to be viewed or edited.
    """
    queryset = Galeria.objects.all()
    serializer_class = GaleriaSerializer

class ReservacionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows galeria to be viewed or edited.
    """
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer