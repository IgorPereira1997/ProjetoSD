from django.shortcuts import render

# Create your views here.

# Páginas customizadas de error da aplicação

def error_400(request, exception):
    return render(request, 'error/400.html', status=400)

def error_403(request, exception):
    return render(request, 'error/403.html', status=403)

def error_404(request, exception):
    return render(request, 'error/404.html', status=404)

def error_500(request):
    return render(request, 'error/500.html', status=500)


