from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import CustomAuthenticationForm


def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'core/login.html'
    next_page = reverse_lazy('core:index')
