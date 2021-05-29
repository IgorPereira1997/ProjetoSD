from django.shortcuts import redirect, render

# Create your views here.

def padrao(request):
    return render(request, 'home/index.html', {})

def sair(request):
    forncedor = request.session['idFornecedor']
    cliente = request.session['idCliente']
    if request.method == "POST":
        request.session['idFornecedor'] = ''
        request.session['idCliente'] = ''
        return redirect('/inicial/home/')
    else:
        return render(request, 'sair/sair.html', {'forn': forncedor, 'cli': cliente})