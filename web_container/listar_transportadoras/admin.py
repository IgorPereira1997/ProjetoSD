from django.contrib import admin
from .models import Transportadoras
# Register your models here.


@admin.register(Transportadoras)
class TransportadorasAdmin(admin.ModelAdmin):
    list_display = ('transportadoraid', 'nometransportadora', 'endereco', 'telefone', 'cidade', 'estado_tag', 'cep', 'cnpj')
    search_fields = ('nometransportadora__icontains', 'cidade__icontains',)
    ordering = ('transportadoraid',)
