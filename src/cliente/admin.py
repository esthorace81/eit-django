from django.contrib import admin

from .models import Cliente, Pais

admin.site.register(Pais)


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'nacimiento', 'pais_origen')
    search_fields = ('nombre', 'apellido')
    list_filter = ('pais_origen',)
