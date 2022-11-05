from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from login.models import Clientes, Fornecedores
from .forms import RecuperarSenhaCliForm, RecuperarSenhaForm, RecuperarSenhaFornForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from ProjetoSD_2 import settings
# Create your views here.

mensagem = 'Usuário ou senha incorretos!'


def login_cliente(request):
    # O login do cliente é feito aqui, fazendo a verificação dos dados de usuário e senha para redirecioná-lo para a listagem de seus produtos
    # e garantindo a deleção de qualquer outra sessão de fornecedores ativa.
    request.session['idFornecedor'] = ''
    if request.method == "POST":
        all_clientes = Clientes.objects.values('usuario', 'senha', 'clienteid')
        validoCliente = 'Diferente'
        usuarioC = request.POST.get('user_cliente')
        senhaC = request.POST.get('key_password_cliente')
        for campo in all_clientes:
            if ((campo['usuario'] == usuarioC) and (campo['senha'] == senhaC)):
                validoCliente = 'Igual'
                request.session['idCliente'] = campo['clienteid']
                return redirect('/listar_produtos/listar/')
        if validoCliente == 'Diferente':
            return render(request, 'cliente/index.html', {'logincliente': validoCliente, 'msg': mensagem, })
    else:
        usuarioC = ''
        senhaC = ''
        validoCliente = ''
        request.session['idCliente'] = ''
        return render(request, 'cliente/index.html', {'logincliente': validoCliente, })


def login_fornecedor(request):
    # Aqui o login do fornecedor é realizado, desativando a sessão do usuário cliente para não haver problemas de um fornecedor acessar a
    # página de clientes, o redirecionando para a listagem de seus produtos.
    request.session['idCliente'] = ''
    if request.method == "POST":
        all_fornecedores = Fornecedores.objects.values('usuario', 'senha', 'fornecedorid')
        validoFornecedor = 'Diferente'
        usuarioF = request.POST.get('user_fornecedor')
        senhaF = request.POST.get('key_password_fornecedor')
        for campo in all_fornecedores:
            if ((campo['usuario'] == usuarioF) and (campo['senha'] == senhaF)):
                validoFornecedor = 'Igual'
                request.session['idFornecedor'] = campo['fornecedorid']
                return redirect('/listar_produtos/listar/')
        if validoFornecedor == 'Diferente':
            return render(request, 'fornecedor/index.html', {'loginfornecedor': validoFornecedor, 'msg': mensagem})
    else:
        usuarioF = ''
        senhaF = ''
        validoFornecedor = ''
        request.session['idFornecedor'] = ''
        return render(request, 'fornecedor/index.html', {'loginfornecedor': validoFornecedor})

# Para a recuperação da senha, será checado o email do requisitante, para saber se o mesmo está cadastrado, se confirmado o cadastro
# E redirecionado um email para o usuário que fez o pedido, para exemplificação, será enviado para o próprio email da empresa, por
# conta dos emails nos cadastros do banco de dados serem inexistentes, e facilitar o teste do projeto. Porém, o email é enviado
# também para o cliente/fornecedor da mesma forma que para a empresa, por fins de teste da função no desenvolvimento. Caso seja
# utilizado o servidor local, há a linha comentada no 'message' que muda o link para o servidor local, caso seja necessário.


def recuperar_senha(request):
    op = request.POST.get('op')
    flag = request.POST.get('flag')
    if op == "1":
        if request.method == "POST" and flag:
            form = RecuperarSenhaCliForm(request.POST)
            if form.is_valid():
                cliente = Clientes.objects.get(email__iexact=request.POST.get('email'))
                subject = "Recuperar Senha"
                body = {
                    'Nome': cliente.nomecompleto,
                    'phonenumber': cliente.telefone,
                    'subject': 'Recuperação de Email do site Transportadora Vietnã',
                    'message': "Por favor, acesse o link '{}{}' para \nconfigurar uma nova senha.".format("http://transportadora-vietna.herokuapp.com/login/finalizar_recovery/?codC=", cliente.clienteid),
                    # "http://127.0.0.1:8000/login/finalizar_recovery/?codC={}"+
                }

                message = "Cliente: {} \n\n\nTelefone: {} \n\nMensagem: {}".format(body.get('Nome'), body.get('phonenumber'), body.get('message'))

                sender = settings.EMAIL_HOST_USER
                recipient = [settings.EMAIL_HOST_USER, cliente.email]

                try:
                    send_mail(subject, message, sender, recipient, fail_silently=True)
                    messages.success(request, "Mensagem Enviada com sucesso!")
                    return render(request, 'recuperar_senha/index.html', {'form': form, 'sucesso': 1, 'forn': 0})
                except BadHeaderError:
                    raise PermissionDenied()
            else:
                return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 0})
        else:
            form = RecuperarSenhaCliForm()
            return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 0})
    elif op == "2":
        if request.method == "POST" and flag:
            form = RecuperarSenhaFornForm(request.POST)
            if form.is_valid():
                fornecedor = Fornecedores.objects.get(email__iexact=request.POST.get('email'))
                subject = "Recuperar Senha"
                body = {
                    'Nome': fornecedor.nomefornecedor,
                    'phonenumber': fornecedor.telefone,
                    'subject': 'Recuperação de Email do site Transportadora Vietnã',
                    'message': "Por favor, acesse o link '{}{}' para \nconfigurar uma nova senha.".format("http://transportadora-vietna.herokuapp.com/login/finalizar_recovery/?codF=", fornecedor.fornecedorid)
                    # "http://127.0.0.1:8000/login/finalizar_recovery/?codF={}"+
                }

                message = ("Fornecedor: {} \n\n\nTelefone: {}\n\nMensagem: {}").format(body.get('Nome'), body.get('phonenumber'), body.get('message'))

                sender = settings.EMAIL_HOST_USER
                recipient = [settings.EMAIL_HOST_USER, fornecedor.email]

                try:
                    send_mail(subject, message, sender, recipient, fail_silently=True)
                    messages.success(request, "Mensagem Enviada com sucesso!")
                    form = RecuperarSenhaFornForm()
                    return render(request, 'recuperar_senha/index.html', {'form': form, 'sucesso': 1, 'forn': 1})
                except BadHeaderError:
                    raise PermissionDenied()
            else:
                return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 1})
        else:
            form = RecuperarSenhaFornForm()
            return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 1})

# Página que será renderizada quando o cliente/fornecedor clicar no login, e identificará se o requisitante é um cliente ou fornecedor,
# recuperando o registro do mesmo e fazendo a alteração de senha. Ao terminar, passa o comando à página de redirecionamento


def finalizar_recovery(request):
    codC = request.GET.get('codC')
    codF = request.GET.get('codF')
    if codC is None and codF is None:
        raise PermissionDenied()
    elif codF is None:  # cliente
        if request.method == "POST":
            form = RecuperarSenhaForm(request.POST)
            if form.is_valid():
                cliente = Clientes.objects.get(clienteid=codC)
                cliente.senha = request.POST.get('novasenha')
                cliente.save(force_update=True)
                return redirect('/login/redirecionar/?l=1')
            else:
                return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 0, 'id': codC})
        else:
            form = RecuperarSenhaForm()
            return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 0, 'id': codC})
    elif codC is None:
        if request.method == "POST":
            form = RecuperarSenhaForm(request.POST)
            if form.is_valid():
                fornecedor = Fornecedores.objects.get(fornecedorid=codF)
                fornecedor.senha = request.POST.get('novasenha')
                fornecedor.save(force_update=True)
                return redirect('/login/redirecionar/?l=2')
            else:
                return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 1, 'id': codF})
        else:
            form = RecuperarSenhaForm()
            return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 1, 'id': codF})
    else:
        raise PermissionDenied()

# Página de redirecionamento após recuperação da senha, permitindo o requisitante voltar para página inicial ou mesmo fazer o login, já com os novos
# dados em funcionamento


def redirecionar(request):
    flag = request.GET.get('l')
    ok = request.GET.get('ok')
    if request.method == "GET" and ok:
        if flag == "2":
            return redirect('/login/fornecedor/')
        elif flag == "1":
            return redirect('/login/cliente/')
    return render(request, 'redirecionar/retornar.html', {'flag': flag})
