import django
from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings

# Create your models here.

class Reservacion(models.Model):
    nombre = models.CharField(max_length = 50,blank=False,default='', verbose_name="Nombre")
    email = models.EmailField(blank=False, verbose_name="Correo Electronico")
    telefono = PhoneNumberField()
    cantidad_personas = models.IntegerField(validators=[MinValueValidator(1)],default=0,blank=False, verbose_name="Cantidad de personas")
    hora_reserva = models.TimeField()
    fecha = models.DateField()
    observacion = models.TextField(blank=True)
    estado_choices = (
        ('CONFIRMADA', 'Confirmada'),
        ('NO_CONFIRMADA', 'No confirmada'),
        ('REALIZADA', 'Realizada'),
        ('CANCELADA', 'Candelada'),
    )
    estado = models.CharField(max_length=30, choices=estado_choices, default='NO_CONFIRMADA')
    motivo = models.TextField(blank=True)


    class Meta:
        verbose_name = 'Reservacion'
        verbose_name_plural = 'Reservaciones'

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombre
