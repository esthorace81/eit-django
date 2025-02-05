from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from producto import models

from ..forms import VentaForm
from ..models import Venta


class VentaListView(ListView):
    model = Venta


class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    success_url = reverse_lazy('producto:venta_list')
