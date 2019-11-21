from django.urls import  include, path
from rest_framework import routers
from api.quickstart import views
 
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'platos', views.PlatoViewSet)
router.register(r'tipoplatos', views.TipoPlatoViewSet)
router.register(r'galeria', views.GaleriaViewSet)
router.register(r'reservacion', views.ReservacionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

