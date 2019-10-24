from django.db import models

# Create your models here.


class Carta(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField(default=0)
    categoria = models.ForeignKey(
        'Categoria', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Carta'
        verbose_name_plural = 'Carta'

    def __str__(self):
        return self.name


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
