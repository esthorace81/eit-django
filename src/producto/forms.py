import dis

from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        # fields = "__all__"
        fields = ['nombre', 'descripcion']

    def clean_descripcion(self):
        descripcion: str = self.cleaned_data.get('descripcion', '')

        if descripcion and len(descripcion) < 3:
            raise forms.ValidationError('La longitud debe ser mayor a 2 caracteres')
        return descripcion


class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'


class VentaForm(forms.ModelForm):
    class Meta:
        model = models.Venta
        fields = ['producto', 'cantidad']
