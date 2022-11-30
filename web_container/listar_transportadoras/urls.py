"""ProjetoSD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'listar_transpotadoras'

urlpatterns = [
    path('adicionar/', views.add_transp, name="add_transp"),
    path('deletar/', views.del_transp, name="del_transp"),
    path('listar/', views.list_transp, name="list_transp"),
    path('atualizar/', views.upd_transp, name="upd_transp"),
    path('adicionar_ini/', views.add_transp_ini, name="add_transp_ini"),
    path('atualizar_ini/', views.upd_transp_ini, name="upd_transp_ini"),
]
