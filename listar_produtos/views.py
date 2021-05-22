from django.shortcuts import render, redirect

from inicial.models import Categorias
from fornecedores.models import Fornecedores
from .models import Produtos
from gerenciar_pedidos.models import Pedidos, PedidosItem
from .forms import AdicionarProdutoForm, AlterarProdutoForm

import inicial.funcoes as func
import os

# Create your views here.

all_categorias = Categorias.objects.values()
all_fornecedores = Fornecedores.objects.values()
forn_list=[]
cat_list=[]
entrega_list=[(5, '5 dias'),(8, '8 dias'), (15, '15 dias'), (30,'30 dias'),]

for campo in all_fornecedores:
    forn_list.append((campo['fornecedorid'], campo['nomefornecedor']),)
    
for campo in all_categorias:
    cat_list.append((campo['categoriaid'], campo['nomecategoria']))

def add_prod(request):
    if request.method == "POST":
        form = AdicionarProdutoForm(forn_list, cat_list, entrega_list, request.POST, request.FILES)
        if form.is_valid():
            Produtos.objects.create(nomeproduto=str(request.POST.get('nomeproduto')),
                                    descricao=str(request.POST.get('descricao')), 
                                    codigobarra=str(request.POST.get('codigobarra')), 
                                    tempoentrega=int(request.POST.get('tempoentrega')),
                                    precorevenda=float(str(request.POST.get('precorevenda')).replace(',', '.')), 
                                    precounitario=float(str(request.POST.get('precounitario')).replace(',', '.')),
                                    estoque=int(request.POST.get('estoque')), 
                                    imagemgrande=func.resize_image(request.FILES.get('foto_grande'), (225, 225)),  
                                    imagempequena=func.resize_image(request.FILES.get('foto_pequena'), (73, 73)), 
                                    fornecedorid=int(request.POST.get('fornecedorid')), 
                                    categoriaid=int(request.POST.get('categoriaid'))
                                    )
            return redirect('/listar_produtos/listar/')
        else:
            form = AdicionarProdutoForm(forn_list, cat_list, entrega_list, request.POST, request.FILES)
            return render(request, 'adicionar/add_prod.html', {'cat': all_categorias, 'forn': all_fornecedores, 'form': form})
    else:
        form = AdicionarProdutoForm(forn_list, cat_list, entrega_list)
        return render(request, 'adicionar/add_prod.html', {'cat': all_categorias, 'forn': all_fornecedores, 'form': form})


def del_prod(request):
    idProduto = request.GET.get('prod')
    produto = Produtos.objects.get(produtoid__exact=idProduto)
    msg = "Você tem certeza que deseja\n apagar o produto do banco de dados?\n"
    if request.method == "POST":
        produto.delete()
        return redirect('/listar_produtos/listar/')
    else:
        return render(request, 'deletar/del_prod.html', {'id': idProduto, 'msg': msg})


def list_prod(request):
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    pesq = request.GET.get('produto')
    if cliente == "" and fornecedor == "":
        return redirect('/inicial/home/')
    else:
        if cliente:
            all_produtos = []
            list_items = []
            qtd = 0
            aux = []
            if Pedidos.objects.filter(clienteid__exact=cliente):
                all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
                all_pedidos_item = PedidosItem.objects.values()
                for linha in all_pedidos:
                    for linha2 in all_pedidos_item:
                        if linha.pedidoid == linha2['pedidoid']:
                            list_items.append((linha2['produtoid'],linha2['quantidade']))
                list_items.sort()
                for i in range(1, len(list_items)):
                    if i == 1:
                        qtd = list_items[i-1][1]
                    if list_items[i-1][0] == list_items[i][0]:
                        qtd += list_items[i][1]
                    else:
                        aux.append((list_items[i-1][0], qtd))
                        if i == len(list_items) - 1:
                            aux.append((list_items[i][0], qtd))
                        else:
                            qtd = list_items[i][1]
                for i in range(0, len(aux)):
                        all_produtos.append(Produtos.objects.get(produtoid=aux[i][0]))
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': False})
            else:
                all_pedidos = None
                print("Cliente não tem prodtuto em estoque")
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': True})
        else:
            if Produtos.objects.filter(fornecedorid__exact=fornecedor):
                if pesq is None:
                    all_produtos = Produtos.objects.filter(fornecedorid__exact=fornecedor)
                else:
                    all_produtos = Produtos.objects.filter(fornecedorid__exact=fornecedor).filter(nomeproduto__icontains=pesq)
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq,'flag': False})
            else:
                all_produtos = None
                print("Fornecedor não tem produtos")
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq,'flag': True})


def upd_prod(request):
    idProduto = request.GET.get('prod')
    produto = Produtos.objects.get(produtoid__exact=idProduto)
    flagChange = False
    if request.method == "POST":
        form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto, request.POST, request.FILES)
        if form.is_valid():
            if produto.nomeproduto   != str(request.POST.get('nomeproduto')):
                produto.nomeproduto   = str(request.POST.get('nomeproduto'))
                flagChange = True
            if produto.descricao     != str(request.POST.get('descricao')):
                produto.descricao     = str(request.POST.get('descricao'))
                flagChange = True
            if produto.codigobarra   != str(request.POST.get('codigobarra')):
                produto.codigobarra   = str(request.POST.get('codigobarra'))
                flagChange = True
            if produto.tempoentrega  != int(request.POST.get('tempoentrega')):
                produto.tempoentrega  = int(request.POST.get('tempoentrega'))
                flagChange = True
            if produto.precorevenda  != float(str(request.POST.get('precorevenda')).replace(',', '.')):
                produto.precorevenda  = float(str(request.POST.get('precorevenda')).replace(',', '.'))
                flagChange = True
            if produto.precounitario != float(str(request.POST.get('precounitario')).replace(',', '.')):
                produto.precounitario = float(str(request.POST.get('precounitario')).replace(',', '.'))
                flagChange = True
            if produto.estoque       != int(request.POST.get('estoque')):
                produto.estoque       = int(request.POST.get('estoque'))
                flagChange = True
            if request.FILES.get('foto_grande') != None:
                produto.imagemgrande  = func.resize_image(request.FILES.get('foto_grande'), (225, 225))
                flagChange = True
            if request.FILES.get('foto_pequena') != None:
                produto.imagempequena = func.resize_image(request.FILES.get('foto_pequena'), (73, 73))
                flagChange = True
            if produto.fornecedorid  != int(request.POST.get('fornecedorid')):
                produto.fornecedorid  = int(request.POST.get('fornecedorid'))
                flagChange = True
            if produto.categoriaid   != int(request.POST.get('categoriaid')):
                produto.categoriaid   = int(request.POST.get('categoriaid'))
                flagChange = True
            if flagChange:
                produto.save(force_update=True)
            return redirect('/listar_produtos/listar/')
        else:
            form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto, request.POST, request.FILES)
            return render(request, 'atualizar/upd_prod.html', {'form': form, 'id': idProduto})
    else:
        form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto)
        return render(request, 'atualizar/upd_prod.html', {'form': form, 'id': idProduto})


def details(request):
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    idProduto = request.GET.get('prod')
    produto = Produtos.objects.filter(produtoid__exact=idProduto)
    qtd = 0
    for i in range(0, len(aux)):
        print(aux[i][0])
        if int(aux[i][0]) == int(idProduto):
            print("entrei")
            qtd = aux[i][1]
            break
        print(qtd)
    return render(request, 'detalhar/details.html', {'prod': produto, 'id': idProduto, 'cliente': cliente, 'forn': fornecedor, 'qtd': qtd})

