from django.shortcuts import render
from clientes.models import Clientes
# Create your views here.

def padrao(request):
    return render(request, 'home/index.html', {})

