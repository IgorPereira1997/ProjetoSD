from django.shortcuts import render, redirect
from clientes.models import Clientes
from fornecedores.models import Fornecedores
# Create your views here.

mensagem = 'Usuário ou senha incorretos!'

def login_cliente(request):
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
                return redirect('/listar_produtos/listar/')
                break
    else:
        usuarioC = ''
        senhaC = ''
        validoCliente = ''
        request.session['idCliente'] = ''
    return render(request, 'cliente/index.html', {'logincliente': validoCliente, 'msg': mensagem, 'sessao': request.session['idCliente']})


def login_fornecedor(request):
    if request.method == "POST":
        all_fornecedores = Fornecedores.objects.values('usuario', 'senha', 'fornecedorid')
        validoFornecedor = 'Diferente'
        usuarioF = request.POST.get('user_fornecedor')
        senhaF = request.POST.get('key_password_fornecedor')
        for campo in all_fornecedores:
            if ((campo['usuario'] == usuarioF) and (campo['senha'] == senhaF)):
                validoFornecedor = 'Igual'
                request.session['idFornecedor'] = campo['fornecedorid']
                request.session['idCliente'] = ''
                return redirect('/listar_transportadoras/listar/')
                break
    else:
        usuarioF = ''
        senhaF = ''
        validoFornecedor = ''
        request.session['idFornecedor'] = ''
    return render(request, 'fornecedor/index.html', {'loginfornecedor': validoFornecedor,'msg': mensagem})