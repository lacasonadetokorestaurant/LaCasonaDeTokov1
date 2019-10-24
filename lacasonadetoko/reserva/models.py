from django.db import models

# Create your models here.


class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    num_person = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'

    def __str__(self):
        return self.nombre
