from django.contrib import admin
from django.urls import path
from . import views

app_name = 'inicial'

urlpatterns = [
    path('home/', views.padrao, name='padrao'),
    path('sair/', views.sair, name="sair"),
]