from django.contrib import admin
from .models import Clientes, Fornecedores, FornecedoresContatos
# Register your models here.

@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nomecompleto', 'email')

@admin.register(Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    list_display = ('fornecedorid', 'nomefornecedor')

@admin.register(FornecedoresContatos)
class FornecedoresContatosAdmin(admin.ModelAdmin):
    list_display = ('fornecedorid', 'nome', 'email')

