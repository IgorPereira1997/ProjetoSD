from django.shortcuts import render, redirect
from login.models import Clientes, Fornecedores
from .forms import RecuperarSenhaCliForm, RecuperarSenhaForm, RecuperarSenhaFornForm
from django.http.response import BadHeaderError
from .forms import ContactMeForm
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
# Create your views here.

mensagem = 'Usuário ou senha incorretos!'

def login_cliente(request):
    request.session['idFornecedor'] = ''
    request.session['idAdmin'] = ''
    if request.method == "POST":
        all_clientes = Clientes.objects.values('usuario', 'senha', 'clienteid')
        validoCliente = 'Diferente'
        usuarioC = request.POST.get('user_cliente')
        senhaC = request.POST.get('key_password_cliente')
        for campo in all_clientes:
            if ((campo['usuario'] == usuarioC) and (campo['senha'] == senhaC)):
                validoCliente = 'Igual'
                request.session['idCliente'] = campo['clienteid']
                request.session['idFornecedor'] = ''
                request.session['idAdmin'] = ''
                return redirect('/listar_produtos/listar/')
        if validoCliente == 'Diferente':
            return render(request, 'cliente/index.html', {'logincliente': validoCliente, 'msg': mensagem,})
    else:
        usuarioC = ''
        senhaC = ''
        validoCliente = ''
        request.session['idCliente'] = ''
        return render(request, 'cliente/index.html', {'logincliente': validoCliente,})


def login_fornecedor(request):
    request.session['idCliente'] = ''
    request.session['idAdmin'] = ''
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
            return render(request, 'fornecedor/index.html', {'loginfornecedor': validoFornecedor,'msg': mensagem})
    else:
        usuarioF = ''
        senhaF = ''
        validoFornecedor = ''
        request.session['idFornecedor'] = ''
        return render(request, 'fornecedor/index.html', {'loginfornecedor': validoFornecedor})

def recuperar_senha(request):
    op = request.POST.get('op')
    if op == "1":
        if request.method == "POST":
            form = RecuperarSenhaCliForm(request.POST)
            if form.is_valid():
                cliente = Clientes.objects.get(email__iexact=request.POST.get('email'))
                subject = "Recuperar Senha"
                body = {
                    'Nome': cliente.nomecompleto,
                    'phonenumber': cliente.telefone,
                    'subject': form.cleaned_data['subject'],
                    'message': "Por favor, acesse o link 'http://127.0.0.1:8000/login/finalizar_recovery/?codC="+ cliente.clienteid + "' para " +
                               "\nconfigurar uma nova senha.",
                }

                message = (
                            "Cliente: " + body.get('Nome') + " " + '\n\n' 
                            + "\nTelefone: " + body.get('phonenumber') + "\n\nMensagem: " + body.get('message')
                        )

                sender = 'transportadoravietna@gmail.com'
                recipient = [cliente.email]

                try:
                    send_mail(subject, message, sender, recipient, fail_silently=True)
                    messages.success(request, "Mensagem Enviada com sucesso!")
                    form = ContactMeForm()
                    return render(request, 'recuperar_senha/index.html', {'form': form, 'sucesso': 1, 'forn': 0})
                except BadHeaderError:
                    return render(request, 'error/500.html', {})
            else:
                return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 0})
        else:
            form = RecuperarSenhaCliForm()
            return render(request, 'recuperar_senha/index.html', {'form': form,'forn': 0})
    elif op == "2":
        if request.method == "POST":
            form = RecuperarSenhaFornForm(request.POST)
            if form.is_valid():
                fornecedor = Fornecedores.objects.get(email__iexact=request.POST.get('email'))
                subject = "Recuperar Senha"
                body = {
                    'Nome': fornecedor.nomecompleto,
                    'phonenumber': fornecedor.telefone,
                    'subject': form.cleaned_data['subject'],
                    'message': "Por favor, acesse o link 'http://127.0.0.1:8000/login/finalizar_recovery/?codF="+ fornecedor.clienteid + "' para " +
                               "\nconfigurar uma nova senha.",
                }

                message = (
                            "Fornecedor: " + body.get('Nome') + " " + '\n\n' 
                            + "\nTelefone: " + body.get('phonenumber') + "\n\nMensagem: " + body.get('message')
                        )

                sender = 'transportadoravietna@gmail.com'
                recipient = [fornecedor.email]

                try:
                    send_mail(subject, message, sender, recipient, fail_silently=True)
                    messages.success(request, "Mensagem Enviada com sucesso!")
                    form = RecuperarSenhaFornForm()
                    return render(request, 'recuperar_senha/index.html', {'form': form, 'sucesso': 1, 'forn': 1})
                except BadHeaderError:
                    return render(request, 'error/500.html', {})
            else:
                return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 1})
        else:
            form = RecuperarSenhaFornForm()
            return render(request, 'recuperar_senha/index.html', {'form': form, 'forn': 1})

def finalizar_recovery(request):
    codC = request.GET.get('codC')
    codF = request.GET.get('codF')
    if codC is None and codF is None:
        return render(request, 'errors/403.html', {})
    elif codF is None:
        if request.method == "POST":
            form = RecuperarSenhaForm(request.POST)
            if form.is_valid():
                cliente = Clientes.objects.get(clienteid=codC)
                cliente.senha = request.POST.get('novasenha')
                cliente.save(force_update=True)
                return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 1, 'forn': 0, 'id': codC})
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
                return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 1, 'forn': 1, 'id': codF})
            else:
                return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 1, 'id': codF})
        else:
            form = RecuperarSenhaForm()
            return render(request, 'finalizar_recovery/index.html', {'form': form, 'sucesso': 0, 'forn': 1, 'id': codF})
    else:
        return render(request, 'errors/403.html', {})


