from django.shortcuts import render, redirect
from inicial.models import Estados
from .models import Transportadoras
import inicial.validators as v
from .forms import AdicionarTransportadoraForm, AdicionarTransportadoraIniForm, AlterarTransportadoraForm
from pycep_correios import get_address_from_cep, WebService

# Create your views here.

all_estados = Estados.objects.values()
estados_list=[]
for campo in all_estados:
    estados_list.append((campo['sigla'], campo['nome']))

dados_preliminares = {}

def add_transp(request):
    if request.method == "POST":
        form = AdicionarTransportadoraForm(estados_list, dados_preliminares,request.POST)
        if form.is_valid():
            id = Estados.objects.get(nome__exact=request.POST.get('estados'))
            Transportadoras.objects.create(nometransportadora=str(request.POST.get('nometransportadora')), endereco=str(request.POST.get('endereco')),
                                           telefone=str(request.POST.get('telefone')), cidade=str(request.POST.get('cidade')), 
                                           estadoid=int(id.estadoid), cep=str(request.POST.get('cep')),
                                           cnpj=str(request.POST.get('cnpj')))
            return redirect('/listar_transportadoras/listar/')
        else:
            form = AdicionarTransportadoraForm(estados_list, dados_preliminares,request.POST)
            return render(request, 'adicionar/add_transp.html', {'form': form})
    else:
        form = AdicionarTransportadoraForm(estados_list, dados_preliminares)
        return render(request, 'adicionar/add_transp.html', {'form': form})

def add_transp_ini(request):
    if request.method == "POST":
        form = AdicionarTransportadoraIniForm(request.POST)
        if form.is_valid():
            dados_preliminares.clear()
            detalhes = get_address_from_cep(str(request.POST.get('cep')), webservice=WebService.VIACEP)
            dados_preliminares['nome']     = request.POST.get('nometransportadora')
            dados_preliminares['cnpj']     = request.POST.get('cnpj')
            dados_preliminares['cep']      = detalhes.get('cep')
            dados_preliminares['telefone'] = request.POST.get('telefone')
            dados_preliminares['estado']   = (Estados.objects.get(sigla__exact=detalhes.get('uf'))).nome
            dados_preliminares['endereco'] = detalhes.get('logradouro')
            dados_preliminares['cidade']   = detalhes.get('cidade')
            return redirect('/listar_transportadoras/adicionar/')
        else:
            form = AdicionarTransportadoraIniForm(request.POST)
            return render(request, 'adicionar_ini/add_transp_ini.html', {'form': form})
    else:
        form = AdicionarTransportadoraIniForm()
        return render(request, 'adicionar_ini/add_transp_ini.html', {'form': form})

    

def upd_transp(request):
    codigo = request.GET.get('codigo')
    flag = False
    if request.method == "POST":
        form = AlterarTransportadoraForm(estados_list, dados_preliminares,request.POST)
        if form.is_valid():
            filial = Transportadoras.objects.get(transportadoraid__exact=codigo)
            id = Estados.objects.get(nome__exact=request.POST.get('estados'))
            if filial.nometransportadora != str(request.POST.get('nometransportadora')):
                filial.nometransportadora = str(request.POST.get('nometransportadora'))
                flag = True
            if filial.endereco != str(request.POST.get('endereco')):
                filial.endereco = str(request.POST.get('endereco'))
                flag = True
            if filial.telefone != str(request.POST.get('telefone')):
                filial.telefone = str(request.POST.get('telefone'))
                flag = True
            if filial.cidade != str(request.POST.get('cidade')):
                filial.cidade = str(request.POST.get('cidade'))
                flag = True
            if filial.estadoid != int(id.estadoid):
                filial.estadoid = int(id.estadoid)
                flag = True
            if filial.cep != str(request.POST.get('cep')):
                filial.cep=str(request.POST.get('cep'))
                flag = True
            if filial.cnpj != str(request.POST.get('cnpj')):
                filial.cnpj = str(request.POST.get('cnpj'))
                flag = True
            if flag:
                filial.save(force_update=True)
            return redirect('/listar_transportadoras/listar/')
        else:
            form = AlterarTransportadoraForm(estados_list, dados_preliminares,request.POST)
            return render(request, 'atualizar/upd_transp.html', {'form': form, 'cod': codigo})
    else:
        form = AlterarTransportadoraForm(estados_list, dados_preliminares)
        return render(request, 'atualizar/upd_transp.html', {'form': form, 'cod': codigo})

def upd_transp_ini(request):
    codigo = request.GET.get('codigo')
    if request.method == "POST":
        form = AdicionarTransportadoraIniForm(None, request.POST)
        if form.is_valid():
            dados_preliminares.clear()
            detalhes = get_address_from_cep(str(request.POST.get('cep')), webservice=WebService.VIACEP)
            dados_preliminares['nome']     = request.POST.get('nometransportadora')
            dados_preliminares['cnpj']     = request.POST.get('cnpj')
            dados_preliminares['cep']      = detalhes.get('cep')
            dados_preliminares['telefone'] = request.POST.get('telefone')
            dados_preliminares['estado']   = (Estados.objects.get(sigla__exact=detalhes.get('uf'))).nome
            dados_preliminares['endereco'] = detalhes.get('logradouro')
            dados_preliminares['cidade']   = detalhes.get('cidade')
            return redirect('/listar_transportadoras/atualizar/?codigo='+codigo)
        else:
            form = AdicionarTransportadoraIniForm(None, request.POST)
            return render(request, 'atualizar_ini/upd_transp_ini.html', {'form': form, 'cod': codigo})
    else:
        filial = Transportadoras.objects.get(transportadoraid__exact=codigo)
        form = AdicionarTransportadoraIniForm(filial)
        return render(request, 'atualizar_ini/upd_transp_ini.html', {'form': form, 'cod': codigo})

def del_transp(request):
    codigo = request.GET.get('codigo')
    filial = Transportadoras.objects.get(transportadoraid__exact=codigo)
    if request.method == "POST":
        filial.delete()
        return redirect('/listar_transportadoras/listar/')
    else:
        dados_preliminares.clear()
        dados_preliminares['nome']     = filial.nometransportadora
        dados_preliminares['cnpj']     = filial.cnpj
        dados_preliminares['cep']      = filial.cep
        dados_preliminares['telefone'] = filial.telefone
        dados_preliminares['estado']   = (Estados.objects.get(estadoid__exact=filial.estadoid)).nome
        dados_preliminares['endereco'] = filial.endereco
        dados_preliminares['cidade']   = filial.cidade
        form = AdicionarTransportadoraForm(estados_list, dados_preliminares)
    return render(request, 'deletar/del_transp.html', {'form': form, 'cod': codigo})

def list_transp(request):
    fornecedor = request.session['idFornecedor']
    all_transportadoras = Transportadoras.objects.all
    return render(request, 'listar/list_transp.html', {'filiais': all_transportadoras})
    