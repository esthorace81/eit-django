from django.shortcuts import render

from . import forms, models


def index(request):
    return render(request, 'producto/index.html')


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'producto/categoria_list.html', context)


def categoria_create(request):
    if request.method == 'GET':
        form = forms.CategoriaForm()
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'producto/categoria_form.html', {'form': form})
