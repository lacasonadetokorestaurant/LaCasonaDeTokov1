from django.db import models

# Create your models here.


class Carrusel(models.Model):
    antetitulo = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50, blank=True)
    imagen = models.ImageField(upload_to='carrusel/')

    class Meta:
        verbose_name = 'Carrusel'
        verbose_name_plural = 'Carrusel'

    def __str__(self):
        return self.titulo
