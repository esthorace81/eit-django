from django.core.exceptions import ValidationError
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def clean(self) -> None:
        self.nombre = f'{self.nombre[0].upper()}{self.nombre[1:]}'
        if len(self.nombre) < 3:
            raise ValidationError('El nombre de la categoría debe tener al menos 3 caracteres')
        if not self.nombre.isalpha():
            raise ValidationError('El nombre de la categoría solo puede contener letras')
        super().clean()
