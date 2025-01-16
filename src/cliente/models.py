from django.db import models


class Pais(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True, blank=True, verbose_name='fecha de nacimiento')
    pais_origen = models.ForeignKey(
        Pais, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='país de origen'
    )

    def __str__(self) -> str:
        return f'{self.apellido}, {self.nombre}'
