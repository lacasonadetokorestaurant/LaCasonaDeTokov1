from django.db import models

# Create your models here.

# SECCION NOSOTROS
class Nosotros(models.Model):
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'

    def __str__(self):
        return self.descripcion


class Contenido(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='nosotros/')
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Contenido'
        verbose_name_plural = 'Contenido'
        ordering = ["-titulo"]

    def __str__(self):
        return self.titulo

# SECCION CARTA
class Plato(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Plato')
    precio = models.IntegerField(default=0, verbose_name='Precio')
    tipo_plato = models.ForeignKey(
        'TipoPlato', on_delete=models.SET_NULL, null=True, verbose_name='Tipo de Plato')
    

    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'
        ordering = ["tipo_plato"]

    def __str__(self):
        return self.nombre


class TipoPlato(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Tipo de Plato')

    class Meta:
        verbose_name = 'Tipo de Plato'
        verbose_name_plural = 'Tipos de Plato'
        

    def __str__(self):
        return self.nombre


# SECCION GALERIA
class Galeria(models.Model):
    titulo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='galeria/')

    class Meta:
        verbose_name = 'Galeria'
        verbose_name_plural = 'Galeria'
        ordering = ["-titulo"]

    def __str__(self):
        return self.titulo
