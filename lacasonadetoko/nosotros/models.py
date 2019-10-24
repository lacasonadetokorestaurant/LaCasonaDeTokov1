from django.db import models

# Create your models here.


class Nosotros(models.Model):
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return self.name


class Contenido(models.Model):
    titulo=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='nosotros/')
    descripcion=models.TextField()
    

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenido'

    def __str__(self):
        return self.name
