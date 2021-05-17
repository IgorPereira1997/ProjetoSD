from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gerenciar_pedidos'

urlpatterns = [
    path('lista_pedidos/', views.listar, name='listarPedidos'),
    path('modificar_pedido/', views.modificar, name='modPedido'),
    path('cancelar_pedido/', views.cancelar, name='cancPedido'),
    path('fazer_pedido/', views.pedir, name='makePedido'),
    path('detalhar_pedido/', views.detalhar, name="detPedido"),
]