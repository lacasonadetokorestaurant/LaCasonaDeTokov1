from django.db import models

# Create your models here.
class Carta(models.Model):
    nombre=models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Carta'
        verbose_name_plural = 'Cartas'

    def __str__(self):
        return self.name
