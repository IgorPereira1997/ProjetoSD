from django.shortcuts import render, redirect
from login.models import Clientes
from listar_transportadoras.models import Transportadoras
from .models import Pedidos, PedidosItem, PedidosStatus
from ProjetoSD_2 import settings
from listar_produtos.models import Produtos
from .forms import PedidoForm, TransportadoraPedidoForm
from inicial.funcoes import gerarConhecimento

# Create your views here.

list_pedidos = []
pedido_final = {}
list_transp = []
all_transportadoras = Transportadoras.objects.values()
for campo in all_transportadoras:
    list_transp.append((campo['transportadoraid'], campo['nometransportadora']),)

def listar(request):
    list_pedidos.clear()
    pedido_final.clear()
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    p = settings.PAYPAL_CLIENT_ID
    if fornecedor == '' and cliente == '':
        return redirect('/inicial/home')
    else:
        all_transportadoras = Transportadoras.objects.all
        all_status = PedidosStatus.objects.all
        if fornecedor != '':
            all_clientes = Clientes.objects.all
            all_pedidos = Pedidos.objects.all
        else:
            all_clientes = Clientes.objects.filter(clienteid__exact=cliente)
            all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
        return render(request, 'lista_pedidos/pedidos.html', {'transportadoras': all_transportadoras, 
                                                              'clientes': all_clientes, 
                                                              'pedidos': all_pedidos,
                                                              'status': all_status, 
                                                              'cli': cliente,
                                                              'paypal': p})

def list_prod(request):
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    pesq = request.GET.get('produto')
    if cliente == "" and fornecedor == "":
        return redirect('/inicial/home/')
    else:
        if cliente:
            if pesq is None:
                all_produtos = Produtos.objects.filter(estoque__gt=0)
            else:
                all_produtos = Produtos.objects.filter(nomeproduto__icontains=pesq)
            return render(request, 'produtos_disp/produtos.html', {'produtos': all_produtos, 'pesq': pesq,'flag': False})
        elif fornecedor:
            return redirect('/listar_transportadoras/listar/')

def details(request):
    cliente = request.session['idCliente']
    if cliente == "":
        return redirect('/inicial/home/')
    elif cliente:
        idProduto = request.GET.get('prod')
        produto = Produtos.objects.get(produtoid__exact=idProduto)
        if request.method == "POST":
            form = PedidoForm(produto.estoque, request.POST)
            if form.is_valid():
                list_pedidos.append({'produtoid': idProduto, 
                                     'clienteid': cliente,
                                     'quantidade':request.POST.get('estoque'),
                                     'transportadoraid': request.POST.get('transportadora'),
                                     'precounitario': produto.precounitario,})
                return redirect('/gerenciar_pedidos/fazer_pedido/')
            else:
                form = PedidoForm(produto.estoque, request.POST)
                return render(request, 'produtos_det/detalhe.html', {'form':form, 'prod': produto, 'id': idProduto, 'cliente': cliente,})
        else:
            form = PedidoForm(produto.estoque)
            return render(request, 'produtos_det/detalhe.html', {'form':form, 'prod': produto, 'id': idProduto, 'cliente': cliente,})
    else:
        return redirect('/inicial/home/')


def modificar(request):
    return render(request, 'modificar_pedido/alterar_status.html', {})

def finalizar(request):
    cliente = request.session['idCliente']
    if cliente == "":
        return redirect('/inicial/home/')
    elif cliente:
        if request.method == "POST":
            form = TransportadoraPedidoForm(list_transp, request.POST)
            if form.is_valid():
                pedido_final['transportadoraid']=request.POST.get('transportadora')
                Pedidos.objects.create(clienteid=pedido_final.get('clienteid'),
                                       data_pedido=pedido_final.get('data_pedido'),
                                       valor_pedido=pedido_final.get('valor_pedido'),
                                       transportadoraid= pedido_final.get('transportadoraid'),
                                       status_pedido=2,
                                       conhecimento=pedido_final.get('conhecimento'))
                for i in range(0, len(list_pedidos)):
                    PedidosItem.objects.create(pedidoid=Pedidos.objects.order_by('pedidoid').values('pedidoid').last().get('pedidoid'),
                                               produtoid=list_pedidos[i].get('produtoid'),
                                               precounitario=list_pedidos[i].get('precounitario'),
                                               quantidade=list_pedidos[i].get('quantidade'),)
                return redirect('/gerenciar_pedidos/lista_pedidos/')
            else:
                form = TransportadoraPedidoForm(list_transp, request.POST)
                return render(request, 'finalizar_pedido/finalizar.html', {'form': form})
        else:
            form = TransportadoraPedidoForm(list_transp)
            return render(request, 'finalizar_pedido/finalizar.html', {'form': form})
    else:
        return redirect('/inicial/home/')


def pedir(request):
    cliente = request.session['idCliente']
    if cliente == "":
        return redirect('/inicial/home/')
    elif cliente:
        msg = "Deseja adicionar outro produto?"
        if request.method == "POST":
            id = 0
            from datetime import datetime
            date_agora = datetime.now().strftime('%Y-%m-%d')
            valor_total = 0.0
            for i in range(0, len(list_pedidos)):
                if i == 0:
                    id = list_pedidos[i]['clienteid']
                valor_total = valor_total + (float(list_pedidos[i]['precounitario'])*float(list_pedidos[i]['quantidade']))
            pedido_final['clienteid'] = id
            pedido_final['data_pedido'] = date_agora
            pedido_final['status_pedido'] = 2
            pedido_final['valor_pedido'] = valor_total
            pedido_final['conhecimento'] = gerarConhecimento()
            return redirect('/gerenciar_pedidos/finalizar_pedido/')
        else:
            return render(request, 'fazer_pedido/realizar_pedido.html', {'msg': msg })
    else:
        return redirect('/inicial/home/')  


def cancelar(request):
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        return redirect('/inicial/home/')
    else:
        msg = "Você tem certeza que deseja cancelar o pedido?"
        idPedido = request.GET.get('order')
        pedido = Pedidos.objects.get(pedidoid__exact=idPedido)
        if request.method == "POST":
            if cliente:
                pedido.status_pedido = 3
            else:
                pedido.status_pedido = 4
            pedido.save(force_update=True)
            return redirect('/gerenciar_pedidos/lista_pedidos/')
        else:
            return render(request, 'cancelar_pedido/cancelar.html', {'id': idPedido, 'msg': msg})

def detalhar(request):
    id = request.GET.get('pedido')
    all_transportadoras = Transportadoras.objects.all
    all_clientes = Clientes.objects.all
    pedido = Pedidos.objects.get(pedidoid=id)
    all_status = PedidosStatus.objects.all
    return render(request, 'detalhar_pedido/detalhar.html', {'transportadoras': all_transportadoras, 'clientes': all_clientes,
                                                             'pedidos': pedido, 'id': id,
                                                             'status': all_status})