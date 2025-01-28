from django.urls import path

from . import views
from .views_models import categoria

app_name = 'producto'

urlpatterns = [
    path('', views.index, name='index'),
    path('categoria/list/', categoria.categoria_list, name='categoria_list'),
    path('categoria/create/', categoria.categoria_create, name='categoria_create'),
    path('categoria/update/<int:pk>', categoria.categoria_update, name='categoria_update'),
    path('categoria/detail/<int:pk>', categoria.categoria_detail, name='categoria_detail'),
    path('categoria/delete/<int:pk>', categoria.categoria_delete, name='categoria_delete'),
]
