from ProjetoSD_2 import settings
from login.models import Fornecedores
from django.utils.safestring import mark_safe
from inicial.models import Categorias
from django.db import models
import os

# Create your models here.


class Produtos(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.SmallIntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.FileField(upload_to='images/product_images/')
    imagempequena = models.FileField(upload_to='images/product_images/')
    fornecedorid = models.SmallIntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.SmallIntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produtos'
        verbose_name = 'Produto do Fornecedor'
        verbose_name_plural = "Produtos Disponíveis (Fornecedores)"

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img src="%s" />' % escape(os.path.join(settings.MEDIA_LINK, str(self.imagempequena))))
    image_tag.short_description = 'Image'

    def categoria_tag(self):
        cat = Categorias.objects.get(categoriaid=self.categoriaid)
        return cat.nomecategoria

    def fornecedor_tag(self):
        forn = Fornecedores.objects.get(fornecedorid=self.fornecedorid)
        return forn.nomefornecedor

    def estoque_str(self):
        if self.estoque != 1:
            return str(self.estoque) + " unidades"
        else:
            return str(self.estoque) + " unidade"

    def precounitario_tag(self):
        return "R$ " + str(self.precounitario).replace('.', ',')

    def precorevenda_tag(self):
        return "R$ " + str(self.precorevenda).replace('.', ',')

    def __str__(self):
        return f"Nome do Produto: {self.nomeproduto} | Código de Barra: {self.codigobarra} | Categoria: {self.categoria_tag}"


class ProdutosClientes(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.SmallIntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.FileField(upload_to='images/product_images_clientes/')
    imagempequena = models.FileField(upload_to='images/product_images_clientes/')
    descontinuado = models.SmallIntegerField(blank=True, null=True)
    fornecedorid = models.SmallIntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.SmallIntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produtos_clientes'
        verbose_name = 'Produto do Cliente'
        verbose_name_plural = "Produtos Disponíveis (Clientes)"

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img src="%s" />' % escape(os.path.join(settings.MEDIA_LINK, str(self.imagempequena))))
    image_tag.short_description = 'Image'

    def categoria_tag(self):
        cat = Categorias.objects.get(categoriaid=self.categoriaid)
        return cat.nomecategoria

    def fornecedor_tag(self):
        forn = Fornecedores.objects.get(fornecedorid=self.fornecedorid)
        return forn.nomefornecedor

    def estoque_str(self):
        if self.estoque != 1:
            return str(self.estoque) + " unidades"
        else:
            return str(self.estoque) + " unidade"

    def precounitario_tag(self):
        return "R$ " + str(self.precounitario).replace('.', ',')

    def precorevenda_tag(self):
        return "R$ " + str(self.precorevenda).replace('.', ',')

    def __str__(self):
        return f"Nome do Produto: {self.nomeproduto} | Código de Barra: {self.codigobarra} | Categoria: {self.categoria_tag}"


class ProdutosStandby(models.Model):
    produtoid = models.IntegerField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.SmallIntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.FileField(upload_to='images/product_images_standby/')
    imagempequena = models.FileField(upload_to='images/product_images_standby/')
    fornecedorid = models.SmallIntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.SmallIntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produtos_standby'
        verbose_name = 'Produto em Negociação'
        verbose_name_plural = "Produtos Disponíveis (Negociações)"

    def image_tag(self):
        from django.utils.html import escape
        return mark_safe('<img src="%s" />' % escape(os.path.join(settings.MEDIA_LINK, str(self.imagempequena))))
    image_tag.short_description = 'Image'

    def categoria_tag(self):
        cat = Categorias.objects.get(categoriaid=self.categoriaid)
        return cat.nomecategoria

    def fornecedor_tag(self):
        forn = Fornecedores.objects.get(fornecedorid=self.fornecedorid)
        return forn.nomefornecedor

    def estoque_str(self):
        if self.estoque != 1:
            return str(self.estoque) + " unidades"
        else:
            return str(self.estoque) + " unidade"

    def precounitario_tag(self):
        return "R$ " + str(self.precounitario).replace('.', ',')

    def precorevenda_tag(self):
        return "R$ " + str(self.precorevenda).replace('.', ',')

    def __str__(self):
        return f"Nome do Produto: {self.nomeproduto} | Código de Barra: {self.codigobarra} | Categoria: {self.categoria_tag}"
