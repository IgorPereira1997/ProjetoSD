# from django.contrib import admin
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('cliente/', views.login_cliente),
    path('fornecedor/', views.login_fornecedor),
    path('recuperar_senha/', views.recuperar_senha),
    path('finalizar_recovery/', views.finalizar_recovery),
    path('redirecionar/', views.redirecionar),
]
