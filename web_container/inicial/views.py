from django.core.exceptions import PermissionDenied
from listar_produtos.models import Produtos, ProdutosClientes, ProdutosStandby
from inicial.models import Estados
from inicial.validators import validadeTelefone
from login.models import Clientes, Fornecedores
from django.shortcuts import redirect, render
from .forms import AdicionarClienteForm, AdicionarClienteIniForm, AdicionarFornecedorForm, AdicionarFornecedorIniForm, AlterarClienteForm, AlterarClienteIniForm, AlterarFornecedorForm, AlterarFornecedorIniForm
from gerenciar_pedidos.models import Pedidos, PedidosItem
# Create your views here.

dados_preliminares = {}


def padrao(request):
    # renderiza a página principal, removendo os logins ativos como medida de segurança.
    request.session['idFornecedor'] = ""
    request.session['idCliente'] = ""
    return render(request, 'home/index.html', {})


def sair(request):
    # faz o logout do cliente/fornecedor, a pedido do cliente/fornecedor
    forncedor = request.session['idFornecedor']
    cliente = request.session['idCliente']
    if request.method == "POST":
        request.session['idFornecedor'] = ''
        request.session['idCliente'] = ''
        return redirect('/')
    else:
        return render(request, 'sair/sair.html', {'forn': forncedor, 'cli': cliente})


def criarPerfilIni(request):
    # inicia o processo de criação do cliente ou fornecedor, requisitando nome, cep, ddd, telefone email para geração dos outros dados do fornecedor/cliente
    # para uso da API pycep-correios para geração dos dados da localização referentes ao cliente/fornecedor e redireciona para a pŕoxima página, com os resultados
    # da requisição alimentando o formulário da criação.
    op = request.POST.get('op')
    if op == '1':  # cliente
        if request.method == "POST" and request.POST.get('flag') == "1":
            form = AdicionarClienteIniForm(request.POST)
            if form.is_valid():
                dados_preliminares['nomecompleto'] = request.POST.get('nomecompleto')
                dados_preliminares['cep'] = request.POST.get('cep')
                dados_preliminares['ddd'] = request.POST.get('ddd')
                dados_preliminares['telefone'] = validadeTelefone(request.POST.get('telefone'))
                dados_preliminares['email'] = request.POST.get('email')
                dados_preliminares['flag'] = '1'
                return redirect('/criar_perfil/')
            else:
                dados_preliminares.clear()
                return render(request, 'criar_perfil_ini/criarini.html', {'forn': 0, 'cli': 1, 'form': form})
        else:
            dados_preliminares.clear()
            form = AdicionarClienteIniForm()
            return render(request, 'criar_perfil_ini/criarini.html', {'forn': 0, 'cli': 1, 'form': form})
    elif op == '2':  # fornecedor
        if request.method == "POST" and request.POST.get('flag') == "1":
            form = AdicionarFornecedorIniForm(request.POST)
            if form.is_valid():
                dados_preliminares['nomefornecedor'] = request.POST.get('nomefornecedor')
                dados_preliminares['cep'] = request.POST.get('cep')
                dados_preliminares['ddd'] = request.POST.get('ddd')
                dados_preliminares['telefone'] = validadeTelefone(request.POST.get('telefone'))
                dados_preliminares['email'] = request.POST.get('email')
                dados_preliminares['flag'] = '2'
                return redirect('/criar_perfil/')
            else:
                dados_preliminares.clear()
                return render(request, 'criar_perfil_ini/criarini.html', {'forn': 1, 'cli': 0, 'form': form})
        else:
            dados_preliminares.clear()
            form = AdicionarFornecedorIniForm()
            return render(request, 'criar_perfil_ini/criarini.html', {'forn': 1, 'cli': 0, 'form': form})


def criarPerfil(request):
    # Aqui o processo de criação do perfil, utilizando dos dados retornados pela api via cep e permitindo mudanças mais finas no endereço, complemento
    # e número referentes ao endereço que o via cep possa não conseguir, além de disponibilizar a criação do login e senha para o cliente/fornecedor. Ao
    # final do processo, o requisitante é redirecionando para a página de login específica do perfil criado (cliente/fornecedor).
    op = dados_preliminares.get('flag')
    if op == '1':
        if request.method == "POST":
            form = AdicionarClienteForm(dados_preliminares, request.POST)
            if form.is_valid():
                estado = Estados.objects.get(nome__exact=request.POST.get("estado"))
                Clientes.objects.create(nomecompleto=request.POST.get('nomecompleto'),
                                        endereco=request.POST.get('endereco'),
                                        complemento=request.POST.get('complemento'),
                                        numero=int(request.POST.get('numero')),
                                        cidade=request.POST.get('cidade'),
                                        estadoid=int(estado.estadoid),
                                        cep=request.POST.get('cep'),
                                        ddd=int(request.POST.get('ddd')),
                                        telefone=request.POST.get('telefone'),
                                        email=request.POST.get('email'),
                                        usuario=request.POST.get('usuario'),
                                        senha=request.POST.get('senha')
                                        )
                dados_preliminares.clear()
                return redirect('/login/cliente/')
            else:
                return render(request, 'criar_perfil/criar.html', {'forn': 0, 'cli': 1, 'form': form})
        else:
            form = AdicionarClienteForm(dados_preliminares)
            return render(request, 'criar_perfil/criar.html', {'forn': 0, 'cli': 1, 'form': form})
    elif op == '2':
        if request.method == "POST":
            form = AdicionarFornecedorForm(dados_preliminares, request.POST)
            if form.is_valid():
                estado = Estados.objects.get(nome__exact=request.POST.get("estado"))
                Fornecedores.objects.create(nomefornecedor=request.POST.get('nomefornecedor'),
                                            endereco=request.POST.get('endereco'),
                                            cidade=request.POST.get('cidade'),
                                            estadoid=int(estado.estadoid),
                                            ddd=request.POST.get('ddd'),
                                            telefone=request.POST.get('telefone'),
                                            usuario=request.POST.get('usuario'),
                                            senha=request.POST.get('senha'),
                                            cep=request.POST.get('cep'),
                                            email=request.POST.get('email'),
                                            )
                dados_preliminares.clear()
                return redirect('/login/fornecedor/')
            else:
                return render(request, 'criar_perfil/criar.html', {'forn': 1, 'cli': 0, 'form': form})
        else:
            form = AdicionarFornecedorForm(dados_preliminares)
            return render(request, 'criar_perfil/criar.html', {'forn': 1, 'cli': 0, 'form': form})


def editarPerfilIni(request):
    # página de edição dos dados do cliente/fornecedor, alimentando a página de coleta de dados inicial de acordo com os dados do cliente/fornecedor
    # cadastrado, e aprovisionando para a operação da api pycep-correios para gerar os dados de localização referentes ao CEP em específico.
    fornecedor = request.session['idFornecedor']
    cliente = request.session['idCliente']
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        if request.method == "POST":
            form = AlterarClienteIniForm(nome, request.POST)
            if form.is_valid():
                dados_preliminares['nomecompleto'] = request.POST.get('nomecompleto')
                dados_preliminares['cep'] = request.POST.get('cep')
                dados_preliminares['ddd'] = request.POST.get('ddd')
                dados_preliminares['telefone'] = validadeTelefone(request.POST.get('telefone'))
                dados_preliminares['email'] = request.POST.get('email')
                return redirect('/editar_perfil/')
            else:
                return render(request, 'editar_perfil_ini/editarini.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto, 'form': form})
        else:
            form = AlterarClienteIniForm(nome)
            return render(request, 'editar_perfil_ini/editarini.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto, 'form': form})
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        if request.method == "POST":
            form = AlterarFornecedorIniForm(nome, request.POST)
            if form.is_valid():
                dados_preliminares['nomefornecedor'] = request.POST.get('nomefornecedor')
                dados_preliminares['cep'] = request.POST.get('cep')
                dados_preliminares['ddd'] = request.POST.get('ddd')
                dados_preliminares['telefone'] = validadeTelefone(request.POST.get('telefone'))
                dados_preliminares['email'] = request.POST.get('email')
                return redirect('/editar_perfil/')
            else:
                return render(request, 'editar_perfil_ini/editarini.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor, 'form': form})
        else:
            form = AlterarFornecedorIniForm(nome)
            return render(request, 'editar_perfil_ini/editarini.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor, 'form': form})


def editarPerfil(request):
    # finaliza a edição dos dados do cliente, e verificando cada campo para atualizar apenas os que tiveram modificação para aliviar o banco de dados
    # e redireciona para a página inicial do perfil, ou seja, a parte de listagem de produtos do usuário.
    fornecedor = request.session['idFornecedor']
    cliente = request.session['idCliente']
    flag = False
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        if request.method == "POST":
            form = AlterarClienteForm(dados_preliminares, nome, request.POST)
            if form.is_valid():
                estado = Estados.objects.get(nome__exact=request.POST.get("estado"))
                if nome.nomecompleto != request.POST.get('nomecompleto'):
                    nome.nomecompleto = request.POST.get('nomecompleto')
                    flag = True
                if nome.endereco != request.POST.get('endereco'):
                    nome.endereco = request.POST.get('endereco')
                    flag = True
                if nome.complemento != request.POST.get('complemento'):
                    nome.complemento = request.POST.get('complemento')
                    flag = True
                if nome.numero != int(request.POST.get('numero')):
                    nome.numero = int(request.POST.get('numero'))
                    flag = True
                if nome.cidade != request.POST.get('cidade'):
                    nome.cidade = request.POST.get('cidade')
                    flag = True
                if nome.estadoid != int(estado.estadoid):
                    nome.estadoid = int(estado.estadoid)
                    flag = True
                if nome.cep != request.POST.get('cep'):
                    nome.cep = request.POST.get('cep')
                    flag = True
                if nome.ddd != int(request.POST.get('ddd')):
                    nome.ddd = int(request.POST.get('ddd'))
                    flag = True
                if nome.telefone != request.POST.get('telefone'):
                    nome.telefone = request.POST.get('telefone')
                    flag = True
                if nome.email != request.POST.get('email'):
                    nome.email = request.POST.get('email')
                    flag = True
                if nome.usuario != request.POST.get('usuario'):
                    nome.usuario = request.POST.get('usuario')
                    flag = True
                if nome.senha != request.POST.get('senha'):
                    nome.senha = request.POST.get('senha')
                    flag = True
                if flag:
                    nome.save(force_update=True)
                dados_preliminares.clear()
                return redirect('/listar_produtos/listar/')
            else:
                return render(request, 'editar_perfil/editar.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto, 'form': form})
        else:
            form = AlterarClienteForm(dados_preliminares, nome)
            return render(request, 'editar_perfil/editar.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto, 'form': form})
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        if request.method == "POST":
            form = AlterarFornecedorForm(dados_preliminares, nome, request.POST)
            if form.is_valid():
                estado = Estados.objects.get(nome__exact=request.POST.get("estado"))
                if nome.nomefornecedor != request.POST.get('nomefornecedor'):
                    nome.nomefornecedor = request.POST.get('nomefornecedor')
                    flag = True
                if nome.endereco != request.POST.get('endereco'):
                    nome.endereco = request.POST.get('endereco')
                    flag = True
                if nome.cidade != request.POST.get('cidade'):
                    nome.cidade = request.POST.get('cidade')
                    flag = True
                if nome.estadoid != int(estado.estadoid):
                    nome.estadoid = int(estado.estadoid)
                    flag = True
                if nome.ddd != request.POST.get('ddd'):
                    nome.ddd = request.POST.get('ddd')
                    flag = True
                if nome.telefone != request.POST.get('telefone'):
                    nome.telefone = request.POST.get('telefone')
                    flag = True
                if nome.email != request.POST.get('email'):
                    nome.email = request.POST.get('email')
                    flag = True
                if nome.usuario != request.POST.get('usuario'):
                    nome.usuario = request.POST.get('usuario')
                    flag = True
                if nome.senha != request.POST.get('senha'):
                    nome.senha = request.POST.get('senha')
                    flag = True
                if nome.cep != request.POST.get('cep'):
                    nome.cep = request.POST.get('cep')
                    flag = True
                if flag:
                    nome.save(force_update=True)
                dados_preliminares.clear()
                return redirect('/listar_produtos/listar/')
            else:
                return render(request, 'editar_perfil/editar.html', {'forn': fornecedor, 'cli': cliente, 'form': form, 'nome': nome.nomefornecedor})
        else:
            form = AlterarFornecedorForm(dados_preliminares, nome)
            return render(request, 'editar_perfil/editar.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor, 'form': form})


def excluirPerfil(request):
    # o usuário pode excluir o seu perfil apenas quando não tem processos pendentes, ou seja, se houverem pedidos abertos o login não pode ser concluído
    # até que todos os pedidos sejam concluidos ou cancelados com sucesso, para impedir inconsistênias no banco de dados.
    fornecedor = request.session['idFornecedor']
    cliente = request.session['idCliente']
    flag = False
    if cliente == "" and fornecedor == "":
        raise PermissionDenied()
    elif cliente:
        nome = Clientes.objects.get(clienteid__exact=cliente)
        if request.method == "POST":
            pedidos_cliente = Pedidos.objects.filter(status_pedido__in=[1, 5, 6]).filter(clienteid__exact=cliente)
            if pedidos_cliente:
                msg = "O(a) Cliente tem pedidos em aberto, não pode ser excluído(a)!"
                return render(request, 'excluir_perfil/excluir.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto, 'msg': msg})
            else:
                pedidos_cliente = Pedidos.objects.filter(status_pedido__in=[2, 7]).filter(clienteid__exact=cliente)
                if pedidos_cliente:
                    for pedido in pedidos_cliente:
                        items = PedidosItem.objects.filter(pedidoid__exact=pedido.pedidoid)
                        for item in items:
                            if pedido.status_pedido == 7:  # já foi entrege
                                prod_cliente = ProdutosClientes.objects.get(produtoid__exact=item.produtoid)
                                prod_cliente.estoque -= int(item.quantidade)
                            elif pedido.status == 2:  # não foi pago
                                prod_standby = ProdutosStandby.objects.get(produtoid=item.produtoid)
                                prod_standby -= int(item.quantidade)
                nome.delete()
                return redirect('/')
        else:
            return render(request, 'excluir_perfil/excluir.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomecompleto})
    elif fornecedor:
        nome = Fornecedores.objects.get(fornecedorid__exact=fornecedor)
        if request.method == "POST":
            produtos_fornecedor = Produtos.objects.filter(fornecedorid__exact=fornecedor)
            produtos_standby_forn = ProdutosStandby.objects.filter(fornecedorid__exact=fornecedor)
            if produtos_standby_forn:
                pedidos_aberto = Pedidos.objects.filter(status_pedido__in=[1, 5, 6])
                for pedido in pedidos_aberto:
                    break1 = False
                    items = PedidosItem.objects.filter(pedidoid__exact=pedido.pedidoid)
                    for item in items:
                        break2 = False
                        for produto in produtos_standby_forn:
                            if item.produtoid == produto.produtoid:
                                flag = True
                                break2 = True
                                break
                        if break2:
                            break1 = True
                            break
                    if break1:
                        break
            if flag:
                msg = "Produtos do fornecedor presentes em pedidos pendentes, não pode ser excluído!"
                return render(request, 'excluir_perfil/excluir.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor})
            else:
                if produtos_fornecedor:
                    produtos_fornecedor.delete()
                if produtos_standby_forn:
                    produtos_standby_forn.delete()
                nome.delete()
                return redirect('/')
        else:
            return render(request, 'excluir_perfil/excluir.html', {'forn': fornecedor, 'cli': cliente, 'nome': nome.nomefornecedor})
