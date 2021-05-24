from django.contrib import admin

from .models import Pedidos, PedidosItem, PedidosStatus
# Register your models here.

@admin.register(Pedidos)
class PedidosAdmin(admin.ModelAdmin):
    pass

@admin.register(PedidosItem)
class PedidosItemAdmin(admin.ModelAdmin):
    pass

@admin.register(PedidosStatus)
class PedidosStatusAdmin(admin.ModelAdmin):
    pass
