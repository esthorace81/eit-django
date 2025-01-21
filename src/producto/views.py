from django.shortcuts import render

from . import models


def index(request):
    return render(request, 'producto/index.html')


def categoria_list(request):
    categorias = models.Categoria.objects.all()
    context = {'categorias': categorias}
    return render(request, 'producto/categoria_list.html', context)
