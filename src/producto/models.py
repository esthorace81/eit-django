from django.core.exceptions import ValidationError
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        ordering = ['nombre']
        verbose_name = 'categoría de productos'
        verbose_name_plural = 'categorías de productos'

    def clean(self) -> None:
        self.nombre = f'{self.nombre[0].upper()}{self.nombre[1:]}'
        if len(self.nombre) < 3:
            raise ValidationError('El nombre de la categoría debe tener al menos 3 caracteres')
        if not self.nombre.isalpha():
            raise ValidationError('El nombre de la categoría solo puede contener letras')
        super().clean()


class Producto(models.Model):
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='categoría'
    )
    nombre = models.CharField(max_length=100, db_index=True)
    descripcion = models.TextField(verbose_name='descripción', null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.FloatField()

    def __str__(self):
        if self.categoria:
            return f'{self.categoria} - {self.nombre}'
        return self.nombre

    class Meta:
        unique_together = ('categoria', 'nombre')
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
