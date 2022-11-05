from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from inicial.models import Categorias
from login.models import Fornecedores, Clientes
from .models import Produtos, ProdutosClientes
from gerenciar_pedidos.models import Pedidos, PedidosItem
from .forms import AdicionarProdutoForm, AlterarProdutoForm
import inicial.funcoes as func
from ProjetoSD_2 import settings
# Create your views here.

# coleta de dados do banco para uso de todas as funções das views, como o banco de categorias disponíveis, dos fornecedores e lista de categorias
all_categorias = Categorias.objects.values()
all_fornecedores = Fornecedores.objects.values()
forn_list = []
cat_list = []
entrega_list = [(5, '5 dias'), (8, '8 dias'), (15, '15 dias'), (30, '30 dias'), ]

for campo in all_fornecedores:
    forn_list.append((campo['fornecedorid'], campo['nomefornecedor']),)

for campo in all_categorias:
    cat_list.append((campo['categoriaid'], campo['nomecategoria']))


def add_prod(request):
    # apenas o fornecedor tem direito de acesso para esta página, já que se um cliente quiser adicionar pedidos, ele deverá realizar um pedido.
    # Aqui, com todos os dados fornecidos, é criado o novo produto para o fornecedor em específico, com uso de uma api de processamento de imagens
    # chamada pillow, e aqui a imagem é formatada para os padrões do site de tamanho de imagens. após adição concluída, o fornecedor volta para a página
    # de listagem de produtos, com o novo produto já adicionado
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
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
                                        imagemgrande=func.resize_image(image=request.FILES.get('foto_grande'), size=(225, 225)),
                                        imagempequena=func.resize_image(image=request.FILES.get('foto_pequena'), size=(73, 73)),
                                        fornecedorid=int(request.POST.get('fornecedorid')),
                                        categoriaid=int(request.POST.get('categoriaid')))
                return redirect('/listar_produtos/listar/')
            else:
                form = AdicionarProdutoForm(forn_list, cat_list, entrega_list, request.POST, request.FILES)
                return render(request, 'adicionar/add_prod.html', {'cat': all_categorias, 'forn': all_fornecedores, 'form': form, 'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomefornecedor})
        else:
            form = AdicionarProdutoForm(forn_list, cat_list, entrega_list)
            return render(request, 'adicionar/add_prod.html', {'cat': all_categorias, 'forn': all_fornecedores, 'form': form, 'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomefornecedor})
    else:
        raise PermissionDenied()


def del_prod(request):
    # página de deleção de produtos, que pode ser feita pelo fornecedor, removendo o produto específico do banco de dados. E negando o acesso se o mesmo
    # for um cliente.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        idProduto = request.GET.get('prod')
        produto = Produtos.objects.get(produtoid__exact=idProduto)
        msg = "Você tem certeza que deseja apagar o produto?"
        if request.method == "POST":
            produto.delete()
            return redirect('/listar_produtos/listar/')
        else:
            return render(request, 'deletar/del_prod.html', {'id': idProduto, 'msg': msg, 'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomefornecedor})
    elif cliente:
        raise PermissionDenied()


def list_prod(request):
    # página inicial após o login, faz a listagem de todos os produtos que o cliente ou fornecedor que acessou a aplicação possui, apenas fazendo o fetch
    # direto nos produtos se for fornecedor e analisando os pedidos finalizados e os items respectivos a eles para preparar a vizualização dos
    # produtos exclusivos do cliente, com ambos podendo fazer pesquisas dentre os seus produtos, por um com o nome como informado na pesquisa
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    pesq = request.GET.get('produto')
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    else:
        if cliente:
            nome = Clientes.objects.get(clienteid__exact=cliente)
            all_produtos = []
            list_items = []
            qtd = 0
            aux = []
            if Pedidos.objects.filter(clienteid__exact=cliente):
                all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
                all_pedidos_item = PedidosItem.objects.values()
                for linha in all_pedidos:
                    for linha2 in all_pedidos_item:
                        if linha.pedidoid == linha2['pedidoid'] and linha.status_pedido == 7:  # verifica se o cliente tem produtos
                            list_items.append((linha2['produtoid'], linha2['quantidade']))
                if len(list_items) == 0:
                    all_pedidos = None
                    return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': True, 'fornecedor': fornecedor,
                                                                     'cliente': cliente, 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
                else:
                    list_items.sort()
                    if len(list_items) == 1:
                        aux = list_items
                    else:
                        for i in range(1, len(list_items)):
                            if i == 1:
                                qtd = list_items[i - 1][1]
                            if list_items[i - 1][0] == list_items[i][0]:
                                qtd += list_items[i][1]
                            else:
                                aux.append((list_items[i - 1][0], qtd))
                                if i == len(list_items) - 1:
                                    aux.append((list_items[i][0], qtd))
                                else:
                                    qtd = list_items[i][1]
                    flagFindProduct = False
                    for i in range(0, len(aux)):
                        try:
                            all_produtos.append(ProdutosClientes.objects.get(produtoid=aux[i][0]))
                            flagFindProduct = True
                        except (ProdutosClientes.objects.get(produtoid=aux[i][0]) is None):
                            continue
                    if flagFindProduct:
                        all_produtos.sort(key=lambda x: x.nomeproduto)
                        if pesq is None:
                            aux = all_produtos
                        else:
                            aux = []
                            from re import search
                            for i in range(0, len(all_produtos)):
                                if search(str(pesq).casefold(), str(all_produtos[i].nomeproduto).casefold()):
                                    aux.append(all_produtos[i])
                        return render(request, 'listar/list_prod.html', {'produtos': aux, 'pesq': pesq, 'flag': False, 'link': settings.MEDIA_LINK,
                                                                         'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomecompleto})
                    else:
                        return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': True, 'fornecedor': fornecedor,
                                                                         'cliente': cliente, 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
            else:
                all_pedidos = None
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': True, 'fornecedor': fornecedor,
                                                                 'cliente': cliente, 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
        elif fornecedor:
            nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
            if Produtos.objects.filter(fornecedorid__exact=fornecedor):
                if pesq is None:
                    all_produtos = Produtos.objects.filter(fornecedorid__exact=fornecedor).order_by('nomeproduto')
                else:
                    all_produtos = Produtos.objects.filter(fornecedorid__exact=fornecedor).filter(nomeproduto__icontains=pesq).order_by('nomeproduto')
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': False, 'fornecedor': fornecedor,
                                                                 'cliente': cliente, 'nome': nome.nomefornecedor, 'link': settings.MEDIA_LINK})
            else:
                all_produtos = None
                return render(request, 'listar/list_prod.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': True, 'fornecedor': fornecedor,
                                                                 'cliente': cliente, 'nome': nome.nomefornecedor, 'link': settings.MEDIA_LINK})


def upd_prod(request):
    # O fornecedor pode atualizar os dados de seus produtos, informando novos dados para o produto selecionado ou mesmo atualizando a quantidade do mesmo
    # em estoque, deixando pelo menos um produto em estoque, já que há a página específica para remoção total do produto. Os dados informados são
    # analisados, fazendo a mudança apenas nos campos que foram realmente modificados.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        idProduto = request.GET.get('prod')
        produto = Produtos.objects.get(produtoid__exact=idProduto)
        flagChange = False
        if request.method == "POST":
            form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto, request.POST, request.FILES)
            if form.is_valid():
                if produto.nomeproduto != str(request.POST.get('nomeproduto')):
                    produto.nomeproduto = str(request.POST.get('nomeproduto'))
                    flagChange = True
                if produto.descricao != str(request.POST.get('descricao')):
                    produto.descricao = str(request.POST.get('descricao'))
                    flagChange = True
                if produto.codigobarra != str(request.POST.get('codigobarra')):
                    produto.codigobarra = str(request.POST.get('codigobarra'))
                    flagChange = True
                if produto.tempoentrega != int(request.POST.get('tempoentrega')):
                    produto.tempoentrega = int(request.POST.get('tempoentrega'))
                    flagChange = True
                if produto.precorevenda != float(str(request.POST.get('precorevenda')).replace(',', '.')):
                    produto.precorevenda = float(str(request.POST.get('precorevenda')).replace(',', '.'))
                    flagChange = True
                if produto.precounitario != float(str(request.POST.get('precounitario')).replace(',', '.')):
                    produto.precounitario = float(str(request.POST.get('precounitario')).replace(',', '.'))
                    flagChange = True
                if produto.estoque != int(request.POST.get('estoque')):
                    produto.estoque = int(request.POST.get('estoque'))
                    flagChange = True
                if request.FILES.get('foto_grande') is not None:
                    produto.imagemgrande = func.resize_image(image=request.FILES.get('foto_grande'), size=(225, 225))
                    flagChange = True
                if request.FILES.get('foto_pequena') is not None:
                    produto.imagempequena = func.resize_image(image=request.FILES.get('foto_pequena'), size=(73, 73))
                    flagChange = True
                if produto.categoriaid != int(request.POST.get('categoriaid')):
                    produto.categoriaid = int(request.POST.get('categoriaid'))
                    flagChange = True
                if flagChange:
                    produto.save(force_update=True)
                return redirect('/listar_produtos/listar/')
            else:
                form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto, request.POST, request.FILES)
                return render(request, 'atualizar/upd_prod.html', {'form': form, 'id': idProduto, 'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomefornecedor})
        else:
            form = AlterarProdutoForm(forn_list, cat_list, entrega_list, produto)
            return render(request, 'atualizar/upd_prod.html', {'form': form, 'id': idProduto, 'fornecedor': fornecedor, 'cliente': cliente, 'nome': nome.nomefornecedor})
    elif cliente:
        raise PermissionDenied()


def details(request):
    # Retorna os dados do produto previamente selecionado, fazendo seu detalhamento. É apenas uma nova busca no banco de produtos, se for um fornecedor
    # acessando a página, e se como cliente, fazendo uma busca mais complexa, envolvendo os pedidos concluídos e seus respectivos itens para mostrar os
    # detalhes e quantidades específicos para o cliente
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        idProduto = request.GET.get('prod')
        produto = Produtos.objects.filter(produtoid__exact=idProduto)
        return render(request, 'detalhar/details.html', {'prod': produto, 'id': idProduto, 'fornecedor': fornecedor, 'cliente': cliente,
                                                         'nome': nome.nomefornecedor, 'link': settings.MEDIA_LINK})
    elif cliente:
        idProduto = request.GET.get('prod')
        nome = Clientes.objects.get(clienteid__exact=cliente)
        produto = ProdutosClientes.objects.filter(produtoid__exact=idProduto)
        qtd = 0
        if Pedidos.objects.filter(clienteid__exact=cliente):
            all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
            all_pedidos_item = PedidosItem.objects.values()
            for linha in all_pedidos:
                for linha2 in all_pedidos_item:
                    if linha.pedidoid == linha2['pedidoid'] and linha.status_pedido == 7:  # verifica se o cliente tem produtos
                        if int(linha2['produtoid']) == int(idProduto):
                            qtd += linha2['quantidade']
        return render(request, 'detalhar/details.html', {'prod': produto, 'id': idProduto, 'fornecedor': fornecedor, 'cliente': cliente,
                                                         'qtd': qtd, 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
