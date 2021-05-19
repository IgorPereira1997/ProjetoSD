from django.shortcuts import render

# Create your views here.

def padrao(request):
    return render(request, 'home/index.html', {})