from django.contrib import admin
from listar_produtos.models import Produtos
from .models import Pedidos, PedidosItem, PedidosStatus
# Register your models here.

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('pedidoid', 'data_pedido', 'valor_pedido')

@admin.register(PedidosItem)
class PedidosItemAdmin(admin.ModelAdmin):
    list_display = ('pedidoid', 'produtoid', 'quantidade')

@admin.register(PedidosStatus)
class PedidosStatusAdmin(admin.ModelAdmin):
    list_display = ('statusid', 'nomestatus')
