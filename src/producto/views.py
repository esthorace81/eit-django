from django.http import HttpRequest
from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, 'producto/index.html')


# *** CATEGORIA - LIST VIEW


def categoria_list(request):
    queryset = models.Categoria.objects.all()
    context = {'object_list': queryset}
    return render(request, 'producto/categoria_list.html', context)


# *** CATEGORIA - CREATE VIEW


def categoria_create(request: HttpRequest):
    if request.method == 'GET':
        form = forms.CategoriaForm()
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})


# *** CATEGORIA - UPDATE VIEW


def categoria_update(request: HttpRequest, pk: int):
    query = models.Categoria.objects.get(id=pk)
    if request.method == 'GET':
        form = forms.CategoriaForm(instance=query)
    if request.method == 'POST':
        form = forms.CategoriaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('producto:categoria_list')
    return render(request, 'producto/categoria_form.html', {'form': form})
