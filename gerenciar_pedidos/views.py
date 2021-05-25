from django.shortcuts import render
from login.models import Clientes
from listar_transportadoras.models import Transportadoras
from .models import Pedidos, PedidosItem, PedidosStatus

# Create your views here.

def listar(request):
    all_transportadoras = Transportadoras.objects.all
    all_clientes = Clientes.objects.all
    all_pedidos = Pedidos.objects.all
    return render(request, 'lista_pedidos/pedidos.html', {'transportadoras': all_transportadoras, 'clientes': all_clientes, 'pedidos': all_pedidos})


def modificar(request):
    return render(request, 'modificar_pedido/alterar_status.html', {})


def pedir(request):
    return render(request, 'fazer_pedido/realizar_pedido.html', {})    


def cancelar(request):
    return render(request, 'cancelar_pedido/cancelar.html', {})

def detalhar(request):
    id = request.GET.get('pedido')
    all_transportadoras = Transportadoras.objects.all
    all_clientes = Clientes.objects.all
    pedido = Pedidos.objects.get(pedidoid=id)
    return render(request, 'detalhar_pedido/detalhar.html', {'transportadoras': all_transportadoras, 'clientes': all_clientes, 'pedidos': pedido})