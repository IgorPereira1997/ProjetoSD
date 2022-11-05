from django.contrib import admin
from .models import Produtos, ProdutosClientes, ProdutosStandby
# Register your models here.


@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    readonly_fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    ordering = ('produtoid',)
    list_display = ('image_tag', 'produtoid', 'nomeproduto', 'estoque_str', 'categoria_tag', 'codigobarra', 'fornecedor_tag',
                    'descricao', 'tempoentrega', 'precorevenda_tag', 'precounitario_tag', )
    search_fields = ("nomeproduto__icontains", )


@admin.register(ProdutosClientes)
class ProdutosClientesAdmin(admin.ModelAdmin):
    fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    readonly_fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    ordering = ('produtoid',)
    list_display = ('image_tag', 'produtoid', 'nomeproduto', 'estoque_str', 'categoria_tag', 'codigobarra', 'fornecedor_tag',
                    'descricao', 'tempoentrega', 'precorevenda_tag', 'precounitario_tag', )
    search_fields = ("nomeproduto__icontains", )


@admin.register(ProdutosStandby)
class ProdutosStandbyAdmin(admin.ModelAdmin):
    fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    readonly_fields = ['image_tag', 'categoria_tag', 'fornecedor_tag']
    ordering = ('produtoid',)
    list_display = ('image_tag', 'produtoid', 'nomeproduto', 'estoque_str', 'categoria_tag', 'codigobarra', 'fornecedor_tag',
                    'descricao', 'tempoentrega', 'precorevenda_tag', 'precounitario_tag', )
    search_fields = ("nomeproduto__icontains", )
