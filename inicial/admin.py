from django.contrib import admin
from .models import Departamentos, Estados, Categorias

# Register your models here.

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
    list_display = ("departamentoid", "nomedepartamento")

@admin.register(Estados)
class EstadosAdmin(admin.ModelAdmin):
    pass

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    pass
