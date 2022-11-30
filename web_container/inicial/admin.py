from django.contrib import admin
from .models import Departamentos, Estados, Categorias

# Register your models here.


@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ("departamentoid", "nomedepartamento")
    exclude = ('created_at',)
    search_fields = ("nomedepartamento",)
    ordering = ('departamentoid',)


@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    list_display = ('estadoid', "sigla", 'nome')
    exclude = ('created_at',)
    ordering = ('estadoid',)
    search_fields = ('sigla', 'nome')
    ordering = ('estadoid',)


@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('categoriaid', 'nomecategoria')
    exclude = ('created_at',)
    search_fields = ('nomecategoria',)
    ordering = ('categoriaid',)
