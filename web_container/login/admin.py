from django.contrib import admin
from .models import Clientes, Fornecedores, FornecedoresContatos
# Register your models here.


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('clienteid', 'nomecompleto', 'endereco', 'complemento', 'numero', 'cidade', 'estado_tag', 'cep', 'ddd', 'telefone', 'email')
    ordering = ('clienteid',)


@admin.register(Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ('fornecedorid', 'nomefornecedor', 'endereco', 'cidade', 'estado_tag', 'cep', 'ddd', 'telefone', 'email')
    ordering = ('fornecedorid',)


@admin.register(FornecedoresContatos)
class FornecedoresContatosAdmin(admin.ModelAdmin):
    list_display = ('contatoid', 'nome', 'empresa', 'departamento', 'telefone', 'email')
    ordering = ('contatoid',)
