from django import forms

from . import models


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = models.Categoria
        # fields = "__all__"
        fields = ['nombre', 'descripcion']

    def clean_descripcion(self):
        descripcion: str = self.cleaned_data.get('descripcion', '')
        if len(descripcion) < 3:
            raise forms.ValidationError('La longitud debe ser mayor a 2 caracteres')
        return descripcion
