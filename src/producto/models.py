from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from core.middleware import request_context


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


class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='usuario')
    telefono = PhoneNumberField(blank=True)
    imagen_perfil = models.ImageField(
        upload_to='perfiles_vendedores', blank=True, null=True, verbose_name='imagen de perfil'
    )

    def __str__(self) -> str:
        return f'{self.user.username} ({self.telefono})'

    class Meta:
        verbose_name = 'vendedor'
        verbose_name_plural = 'vendedores'


class Venta(models.Model):
    vendedor = models.ForeignKey(
        Vendedor, on_delete=models.PROTECT, editable=False, blank=True, null=True
    )
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.FloatField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    fecha_venta = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self) -> str:
        vendedor_username = self.vendedor.user.username if self.vendedor else 'Sin vendedor'
        return f'{vendedor_username} - {self.producto.nombre} ${self.precio_total}'

    def clean(self):
        # Validar que el usuario actual sea vendedor
        request = request_context.get()
        if request and request.user.is_authenticated:
            if not hasattr(request.user, 'vendedor'):
                raise ValidationError('El usuario no tiene un perfil de vendedor asociado')
        else:
            raise ValidationError('Se requiere autenticación para crear ventas')

        if self.cantidad > self.producto.stock:
            raise ValidationError({'cantidad': ['No hay suficiente stock para realizar la venta.']})
        # Validar que la cantidad sea mayor a 0
        if self.cantidad <= 0:
            raise ValidationError({'cantidad': ['La cantidad debe ser mayor a 0.']})
        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        if not self.vendedor:
            request = request_context.get()
            if request and request.user.is_authenticated:
                self.vendedor, _ = Vendedor.objects.get_or_create(user=request.user)

        self.precio_total = float(self.producto.precio) * self.cantidad
        if self.pk is None:
            self.producto.stock -= self.cantidad
            self.producto.save()
        super().save(*args, **kwargs)
