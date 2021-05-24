from django.contrib import admin
from .models import Produtos
# Register your models here.

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    pass
