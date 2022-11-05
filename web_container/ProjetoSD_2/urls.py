"""ProjetoSD_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.models import Group

admin.site.site_header = "Transportadora Vietnã"
admin.site.site_url = "/"
admin.site.site_title = "Administração da Transportadora Vietnã"

handler404 = 'errors.views.error_404'
handler500 = 'errors.views.error_500'
handler403 = 'errors.views.error_403'
handler400 = 'errors.views.error_400'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contato/', include('contato.urls')),
    # path('franquias/', include('franquias.urls')),
    path('listar_produtos/', include('listar_produtos.urls')),
    path('listar_transportadoras/', include('listar_transportadoras.urls')),
    path('login/', include('login.urls')),
    path('gerenciar_pedidos/', include('gerenciar_pedidos.urls')),
    path('', include('inicial.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
