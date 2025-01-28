from django.http import HttpRequest
from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, 'producto/index.html')
