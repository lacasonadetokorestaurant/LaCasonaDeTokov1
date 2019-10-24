from django.db import models

# Create your models here.
class Galeria(models.Model):
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='galeria/')

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'

    def __str__(self):
        return self.name
