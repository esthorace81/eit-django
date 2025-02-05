from django.contrib import messages
from django.contrib.auth.decorators import login_not_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ValidationError
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
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

    def form_valid(self, form):
        form.instance.vendedor = self.request.user.vendedor
        return super().form_valid(form)
