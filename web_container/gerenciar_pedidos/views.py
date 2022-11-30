import os
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from login.models import Clientes, Fornecedores
from listar_transportadoras.models import Transportadoras
from .models import Pedidos, PedidosItem, PedidosStatus
from ProjetoSD_2 import settings
from listar_produtos.models import Produtos, ProdutosStandby, ProdutosClientes
from .forms import PedidoForm, TransportadoraPedidoForm
from inicial.funcoes import gerarConhecimento
import json
import inicial.funcoes as func

# Create your views here.

list_pedidos = []
pedido_final = {}


def listar(request):
    list_pedidos.clear()
    pedido_final.clear()
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if fornecedor == '' and cliente == '':
        raise PermissionDenied()
    # Procura saber se realmente o usuário está logado ao acessar a página, em caso de erro ele é redirecionado para a página de acesso proibido.
    else:
        # Coleta de todas as transportadoras e dos status do pedido, por servir para ambos fornecedor e cliente.
        all_transportadoras = Transportadoras.objects.all
        all_status = PedidosStatus.objects.all
        if fornecedor:
            # percorre todos os pedidos e seus itens, formando uma lista que será enviada para a página com os pedidos exclusivos envolvendo
            # produtos do fornecedor
            empresa = Fornecedores.objects.get(fornecedorid=fornecedor)
            all_pedidos = []
            all_clientes = Clientes.objects.all
            pedidos = Pedidos.objects.values()
            all_items = PedidosItem.objects.values()
            produtos = Produtos.objects.filter(fornecedorid__exact=fornecedor)
            for item in all_items:
                for pedido in pedidos:
                    for produto in produtos:
                        if item.get('pedidoid') == pedido.get('pedidoid') and produto.produtoid == item.get('produtoid') and all_pedidos.count(pedido) < 1:
                            all_pedidos.append(pedido)
            return render(request, 'lista_pedidos/pedidos.html', {'transportadoras': all_transportadoras,
                                                                  'clientes': all_clientes,
                                                                  'pedidos': all_pedidos,
                                                                  'status': all_status,
                                                                  'forn': fornecedor,
                                                                  'cli': cliente,
                                                                  'nome': empresa.nomefornecedor})
        else:
            # Como a página de redirecionamento após pagamento, tenta ver se houve envio de dados pela API do paypal informando o pagamento
            # para fazer a modificação do status. Caso não tenha, o código procede normalmente, fazendo a busca de pedidos referente ao cliente
            # acessando a aplicação.
            nome = Clientes.objects.get(clienteid__exact=cliente)
            all_clientes = Clientes.objects.filter(clienteid__exact=cliente)
            all_pedidos = Pedidos.objects.filter(clienteid__exact=cliente)
            try:
                body = json.loads(request.body)
                pedido = Pedidos.objects.get(pedidoid__exact=body['pedidoid'])
                pedido.status_pedido = body['status']
                pedido.save(force_update=True)
            except pedido.DoesNotExist:
                pass
            return render(request, 'lista_pedidos/pedidos.html', {'transportadoras': all_transportadoras,
                                                                  'clientes': all_clientes,
                                                                  'pedidos': all_pedidos,
                                                                  'status': all_status,
                                                                  'forn': fornecedor,
                                                                  'cli': cliente,
                                                                  'nome': nome.nomecompleto})


def list_prod(request):
    # Verificação se há um login válido para um cliente, caso contrário levanta um acesso negado. Caso seja um cliente,
    # há o fetch para todos os produtos disponíveis para compra, com filtro se o cliente procurar por um produto
    # com nome específico pela janela de pesquisa.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    pesq = request.GET.get('produto')
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    else:
        if cliente:
            nome = Clientes.objects.get(clienteid=cliente)
            if pesq is None:
                all_produtos = Produtos.objects.filter(estoque__gt=0).order_by('nomeproduto')
            else:
                all_produtos = Produtos.objects.filter(estoque__gt=0).filter(nomeproduto__icontains=pesq).order_by('nomeproduto')
            return render(request, 'produtos_disp/produtos.html', {'produtos': all_produtos, 'pesq': pesq, 'flag': False, 'forn': fornecedor,
                                                                   'cli': cliente, 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
        elif fornecedor:
            raise PermissionDenied()


def details(request):
    # Continuação do pedido, novamente apenas o cliente pode acessar a página. Ela é acessada ao se clicar em um produto específico, mostrando
    # Seus dados completos e perguntando a quantidade que poderá ser requisitada, e depois disso redireciona para a página de
    # finalização do pedido, guardando os dados daquele pedido em uma lista que funciona com carrinho.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        idProduto = request.GET.get('prod')
        produto = Produtos.objects.get(produtoid__exact=idProduto)
        if request.method == "POST":
            form = PedidoForm(produto.estoque, request.POST)
            if form.is_valid():
                list_pedidos.append({'produtoid': idProduto,
                                     'clienteid': cliente,
                                     'quantidade': request.POST.get('estoque'),
                                     'transportadoraid': request.POST.get('transportadora'),
                                     'precounitario': produto.precounitario, })
                return redirect('/gerenciar_pedidos/fazer_pedido/')
            else:
                form = PedidoForm(produto.estoque, request.POST)
                return render(request, 'produtos_det/detalhe.html', {'form': form, 'prod': produto, 'id': idProduto, 'cli': cliente, 'forn': fornecedor,
                                                                     'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})
        else:
            form = PedidoForm(produto.estoque)
            return render(request, 'produtos_det/detalhe.html', {'form': form, 'prod': produto, 'id': idProduto, 'cli': cliente, 'forn': fornecedor,
                                                                 'nome': nome.nomecompleto, 'link': settings.MEDIA_LINK})


def modificar(request):
    # Primeiro verifica-se se um login válido está ativo. O fornecedor acessa a página a partir do pedido pago, onde confirma o pagamento alterando
    # o status para aguardando envio e assim por diante até a entrega. O dia de cada operação é salvo no pedido, e se concluído, faz a transferência
    # do banco de produtos reservados para o cliente final.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    pedido = request.GET.get('pedido')
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        list_status = []
        list_status.clear()
        flag = request.POST.get('flag')
        pedido_change = Pedidos.objects.get(pedidoid__exact=pedido)
        msg = "Deseja confirmar que o pedido foi "
        if pedido_change.status_pedido == 1:
            msg += "pago?"
        elif pedido_change.status_pedido == 5:
            msg += "enviado?"
        elif pedido_change.status_pedido == 6:
            msg += "entregue?"
        if request.method == "POST" and flag == "1":
            status = pedido_change.status_pedido
            if status == 1:
                pedido_change.status_pedido = 5
            elif status == 5 or status == 6:
                pedido_change.status_pedido += 1
                from datetime import datetime
                if status == 5:
                    pedido_change.data_saida = datetime.now().strftime('%Y-%m-%d')
                if status == 6:
                    pedido_change.data_entrega = datetime.now().strftime('%Y-%m-%d')
                    pedido_item = PedidosItem.objects.get(pedidoid__exact=pedido_change.pedidoid)
                    standby = ProdutosStandby.objects.get(produtoid__exact=pedido_item.produtoid)
                    try:
                        prod_cliente = ProdutosClientes.objects.get(produtoid__exact=pedido_item.produtoid)
                        prod_cliente.estoque += int(standby.estoque)
                        prod_cliente.save(force_update=True)
                    except prod_cliente.DoesNotExist:
                        import urllib
                        imageG = os.path.join(settings.BASE_DIR, "imgg.jpg")
                        imageP = os.path.join(settings.BASE_DIR, "imgp.jpg")
                        urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, standby.imagemgrande), imageG)
                        urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, standby.imagempequena), imageP)

                        ProdutosClientes.objects.create(produtoid=standby.produtoid,
                                                        nomeproduto=standby.nomeproduto,
                                                        descricao=standby.descricao,
                                                        codigobarra=standby.codigobarra,
                                                        tempoentrega=standby.tempoentrega,
                                                        precorevenda=standby.precorevenda,
                                                        precounitario=standby.precounitario,
                                                        estoque=int(pedido_item.quantidade),
                                                        imagemgrande=func.resize_image(image=imageG, size=(225, 225), mod_image=1),
                                                        imagempequena=func.resize_image(image=imageP, size=(73, 73), mod_image=1),
                                                        fornecedorid=standby.fornecedorid,
                                                        categoriaid=standby.categoriaid
                                                        )
                    if standby.estoque == int(pedido_item.quantidade):
                        standby.delete()
                    else:
                        standby.estoque -= int(pedido_item.quantidade)
                        standby.save(force_update=True)
            pedido_change.save(force_update=True)
            return redirect('/gerenciar_pedidos/lista_pedidos/')
        else:
            return render(request, 'modificar_pedido/alterar_status.html', {'id': pedido, 'cli': cliente, 'forn': fornecedor, 'msg': msg, 'nome': nome.nomefornecedor})
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        valor = request.POST.get('valorPedido')
        return render(request, 'modificar_pedido/alterar_status.html',
                      {'id': pedido, 'valor': valor.replace(',', '.'),
                       'cli': cliente, 'forn': fornecedor,
                       'nome': nome.nomecompleto, 'valor_show': valor})


def finalizar(request):
    # Apenas o cliente pode acessar a página, quando ele finaliza o pedido, a lista "carrinho" é analisada para fazer a reserva de produtos, tirando
    # a quantidade do produto da lista do fornecedor dono de cada produto e estocando na lista de produtos reservados, cirando o produto ou apenas
    # aumentando o estoque total e a função redireciona para a página de pedidos do cliente.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        list_transp = []
        all_transportadoras = Transportadoras.objects.values()
        for campo in all_transportadoras:
            list_transp.append((campo['transportadoraid'], campo['nometransportadora']),)
        if request.method == "POST":
            form = TransportadoraPedidoForm(list_transp, request.POST)
            if form.is_valid():
                pedido_final['transportadoraid'] = request.POST.get('transportadora')
                Pedidos.objects.create(clienteid=pedido_final.get('clienteid'),
                                       data_pedido=pedido_final.get('data_pedido'),
                                       valor_pedido=pedido_final.get('valor_pedido'),
                                       transportadoraid=pedido_final.get('transportadoraid'),
                                       status_pedido=2,
                                       conhecimento=pedido_final.get('conhecimento'))
                for i in range(0, len(list_pedidos)):
                    PedidosItem.objects.create(pedidoid=Pedidos.objects.order_by('pedidoid').values('pedidoid').last().get('pedidoid'),
                                               produtoid=list_pedidos[i].get('produtoid'),
                                               precounitario=list_pedidos[i].get('precounitario'),
                                               quantidade=list_pedidos[i].get('quantidade'),)

                    produto_alvo = Produtos.objects.get(produtoid__exact=list_pedidos[i].get('produtoid'))

                    try:
                        standby = ProdutosStandby.objects.get(produtoid__exact=list_pedidos[i].get('produtoid'))
                        standby.estoque += int(list_pedidos[i].get('quantidade'))
                        standby.save(force_update=True)
                    except standby.DoesNotExist:
                        import urllib
                        imageG = os.path.join(settings.BASE_DIR, "imgg.jpg")
                        imageP = os.path.join(settings.BASE_DIR, "imgp.jpg")
                        urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, produto_alvo.imagemgrande), imageG)
                        urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, produto_alvo.imagempequena), imageP)

                        ProdutosStandby.objects.create(produtoid=produto_alvo.produtoid,
                                                       nomeproduto=produto_alvo.nomeproduto,
                                                       descricao=produto_alvo.descricao,
                                                       codigobarra=produto_alvo.codigobarra,
                                                       tempoentrega=produto_alvo.tempoentrega,
                                                       precorevenda=produto_alvo.precorevenda,
                                                       precounitario=produto_alvo.precounitario,
                                                       estoque=int(list_pedidos[i].get('quantidade')),
                                                       imagemgrande=func.resize_image(image=imageG, size=(225, 225), mod_image=1),
                                                       imagempequena=func.resize_image(image=imageP, size=(73, 73), mod_image=1),
                                                       fornecedorid=produto_alvo.fornecedorid,
                                                       categoriaid=produto_alvo.categoriaid)
                    produto_alvo.estoque -= int(list_pedidos[i].get('quantidade'))
                    produto_alvo.save(force_update=True)

                return redirect('/gerenciar_pedidos/lista_pedidos/')
            else:
                form = TransportadoraPedidoForm(list_transp, request.POST)
                return render(request, 'finalizar_pedido/finalizar.html', {'form': form, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto})
        else:
            form = TransportadoraPedidoForm(list_transp)
            return render(request, 'finalizar_pedido/finalizar.html', {'form': form, 'forn': fornecedor, 'cli': cliente})


def pedir(request):
    # somente o cliente pode acessar essa paǵina, e nela o pedido é então finalizado, contabilizando o valor total de todos os produtos na lista
    # emulando o carrinho e criando o pedido final, gerando seus dados e redirecionando para a página de finalização para processamento da transportadora
    # que fará a entrega do pedido e outros processamentos pós-pedido
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        msg = "Deseja adicionar outro produto?"
        if request.method == "POST":
            id = 0
            from datetime import datetime
            date_agora = datetime.now().strftime('%Y-%m-%d')
            valor_total = 0.0
            for i in range(0, len(list_pedidos)):
                if i == 0:
                    id = list_pedidos[i]['clienteid']
                valor_total = valor_total + (float(list_pedidos[i]['precounitario']) * float(list_pedidos[i]['quantidade']))
            pedido_final['clienteid'] = id
            pedido_final['data_pedido'] = date_agora
            pedido_final['status_pedido'] = 2
            pedido_final['valor_pedido'] = valor_total
            pedido_final['conhecimento'] = gerarConhecimento()
            return redirect('/gerenciar_pedidos/finalizar_pedido/')
        else:
            return render(request, 'fazer_pedido/realizar_pedido.html', {'msg': msg, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto})


def cancelar(request):
    # Aqui, como o próprio nome diz, o pedido pode ser cancelado e é "fechado", mudando seu status para cancelado pelo cliente ou pela empresa,
    # Dependendo de quem requisitou o cancelamento do mesmo e então, a página redireciona para a listagem dos pedidos do cliente/fornecedor
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    else:
        msg = "Você tem certeza que deseja cancelar o pedido?"
        idPedido = request.GET.get('order')
        pedido = Pedidos.objects.get(pedidoid__exact=idPedido)
        if request.method == "POST":
            if cliente:
                pedido.status_pedido = 3
            else:
                pedido.status_pedido = 4
            pedido_items = PedidosItem.objects.filter(pedidoid__exact=pedido.pedidoid)
            for item in pedido_items:
                standby = ProdutosStandby.objects.get(produtoid__exact=item.produtoid)
                try:
                    prod_fornecedor = Produtos.objects.get(produtoid__exact=item.produtoid)
                    prod_fornecedor.estoque += int(standby.estoque)
                    prod_fornecedor.save(force_update=True)
                except prod_fornecedor.DoesNotExist:
                    import urllib
                    imageG = os.path.join(settings.BASE_DIR, "imgg.jpg")
                    imageP = os.path.join(settings.BASE_DIR, "imgp.jpg")
                    urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, prod_fornecedor.imagemgrande), imageG)
                    urllib.request.urlretrieve("%s%s" % (settings.MEDIA_LINK, prod_fornecedor.imagempequena), imageP)

                    Produtos.objects.create(produtoid=standby.produtoid,
                                            nomeproduto=standby.nomeproduto,
                                            descricao=standby.descricao,
                                            codigobarra=standby.codigobarra,
                                            tempoentrega=standby.tempoentrega,
                                            precorevenda=standby.precorevenda,
                                            precounitario=standby.precounitario,
                                            estoque=int(item.quantidade),
                                            imagemgrande=func.resize_image(image=imageG, size=(225, 225), mod_image=1),
                                            imagempequena=func.resize_image(image=imageP, size=(73, 73), mod_image=1),
                                            fornecedorid=standby.fornecedorid,
                                            categoriaid=standby.categoriaid
                                            )
                if standby.estoque == int(item.quantidade):
                    standby.delete()
                else:
                    standby.estoque -= int(item.quantidade)
                    standby.save(force_update=True)
            from datetime import datetime
            pedido.data_entrega = datetime.now().strftime('%Y-%m-%d')
            pedido.save(force_update=True)
            return redirect('/gerenciar_pedidos/lista_pedidos/')
        else:
            if cliente:
                nome = Clientes.objects.get(clienteid__exact=cliente)
                return render(request, 'cancelar_pedido/cancelar.html', {'id': idPedido, 'msg': msg, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto})
            else:
                nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
                return render(request, 'cancelar_pedido/cancelar.html', {'id': idPedido, 'msg': msg, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor})


def detalhar(request):
    # pode ser acessado por ambos fornecedor e cliente, e aqui o pedido que fez o 'trigger' desta página tem todos os seus detalhes mostrado, como
    # data de criação, data de envio e/ou data de cancelamento/entrega, entre outros, e em tal página tem o redirecionamentos para cancelar o pedido,
    # realizar o pagamento (disponível apenas para clientes) ou voltar para página principal dos pedidos.
    cliente = request.session['idCliente']
    fornecedor = request.session['idFornecedor']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    else:
        id = request.GET.get('pedido')
        all_transportadoras = Transportadoras.objects.all
        all_clientes = Clientes.objects.all
        pedido = Pedidos.objects.get(pedidoid=id)
        all_status = PedidosStatus.objects.all
        if cliente:
            nome = Clientes.objects.get(clienteid__exact=cliente)
            return render(request, 'detalhar_pedido/detalhar.html', {'transportadoras': all_transportadoras, 'clientes': all_clientes, 'pedidos': pedido, 'id': id,
                                                                     'status': all_status, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto,
                                                                     'link': settings.MEDIA_LINK})
        elif fornecedor:
            nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
            return render(request, 'detalhar_pedido/detalhar.html', {'transportadoras': all_transportadoras, 'clientes': all_clientes, 'pedidos': pedido, 'id': id,
                                                                     'status': all_status, 'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor,
                                                                     'link': settings.MEDIA_LINK})
