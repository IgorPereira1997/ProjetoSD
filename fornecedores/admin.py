from django.contrib import admin
from .models import Fornecedores, FornecedoresContatos
# Register your models here.

@admin.register(Fornecedores)
class FornecedoresAdmin(admin.ModelAdmin):
    pass
@admin.register(FornecedoresContatos)


class FornecedoresContatosAdmin(admin.ModelAdmin):
    pass
