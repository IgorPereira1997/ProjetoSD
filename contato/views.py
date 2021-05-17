from django.shortcuts import render

# Create your views here.

def fale_conosco(request):
    return render(request, 'contato.html', {})