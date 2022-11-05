# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicial'

urlpatterns = [
    path('', views.padrao, name='padrao'),
    path('sair/', views.sair, name="sair"),
    path('criar_perfil/', views.criarPerfil, name="criarPerfil"),
    path('editar_perfil/', views.editarPerfil, name="editarPerfil"),
    path('excluir_perfil/', views.excluirPerfil, name="excluirPerfil"),
    path('criar_perfil_ini/', views.criarPerfilIni, name="criarPerfilIni"),
    path('editar_perfil_ini/', views.editarPerfilIni, name="editarPerfilIni"),
]
