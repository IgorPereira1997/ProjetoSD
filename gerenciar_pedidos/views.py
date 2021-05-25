from django.shortcuts import render, redirect
from login.models import Clientes
from listar_transportadoras.models import Transportadoras
from .models import Pedidos, PedidosItem, PedidosStatus

# Create your views here.

def listar(request):
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if fornecedor == '' and cliente == '':
        return redirect('/inicial/home')
    else:
        all_transportadoras = Transportadoras.objects.all
        if fornecedor != '':
            all_clientes = Clientes.objects.all
            all_pedidos = Pedidos.objects.filter(transportadoraid__exact=fornecedor)
        else:
            all_clientes = Clientes.objects.filter(clienteid__exact=cliente)
            all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
        return render(request, 'lista_pedidos/pedidos.html', {'transportadoras': all_transportadoras, 
                                                              'clientes': all_clientes, 
                                                              'pedidos': all_pedidos, 
                                                              'cli': cliente})


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