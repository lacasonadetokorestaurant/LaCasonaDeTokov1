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

    def __str__(self):
        return self.titulo

# SECCION CARTA
class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    tipo_plato = models.ForeignKey(
        'TipoPlato', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Plato'
        verbose_name_plural = 'Platos'

    def __str__(self):
        return self.nombre


class TipoPlato(models.Model):
    nombre = models.CharField(max_length=50)

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

    def __str__(self):
        return self.titulo
