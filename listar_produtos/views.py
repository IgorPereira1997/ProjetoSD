from django.shortcuts import render, redirect

from inicial.models import Categorias
from fornecedores.models import Fornecedores
from .models import Produtos
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
        return render(request, 'deletar/del_prod.html', {'id': idProduto, 'msg':msg})


def list_prod(request):
    cliente = request.session['idCliente']
    pesq = request.GET.get('produto')
    if pesq is None: 
        all_produtos = Produtos.objects.all
    else:
        all_produtos = Produtos.objects.filter(nomeproduto__icontains=pesq)
    return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq,})


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
    idProduto = request.GET.get('prod')
    produto = Produtos.objects.filter(produtoid__exact=idProduto)
    return render(request, 'detalhar/details.html', {'prod': produto, 'id': idProduto})

