from django.contrib import admin
from .models import Pedidos, PedidosItem, PedidosStatus
# Register your models here.


@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    list_display = ('pedidoid', 'cliente_tag', 'transportadora_tag',
                    'data_pedido', 'data_saida', 'data_entrega',
                    'status_tag', 'valor', 'conhecimento')
    exclude = ('created_at',)
    search_fields = ('pedidoid', 'clienteid', 'status_pedido', 'data_pedido')
    ordering = ('pedidoid',)


@admin.register(PedidosItem)
class PedidosItemAdmin(admin.ModelAdmin):
    list_display = ('pedidoid', 'image_tag', 'produto_tag',
                    'quantidade_str', 'precounitario_tag')
    exclude = ('created_at',)
    search_fields = ('pedidoid', 'produtoid', 'quantidade')
    ordering = ('pedidoid',)


@admin.register(PedidosStatus)
class PedidosStatusAdmin(admin.ModelAdmin):
    list_display = ('statusid', 'nomestatus')
    exclude = ('created_at',)
    search_fields = ('statusid', 'nomestatus__icontains')
    ordering = ('statusid',)
