from django.db import models

# Create your models here.

class Produtos(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.SmallIntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.FileField(max_length=100)
    imagempequena = models.FileField(max_length=100)
    fornecedorid = models.SmallIntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.SmallIntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produtos'
        verbose_name = 'Produto do Fornecedor'
        verbose_name_plural  =  "Produtos Disponíveis (Fornecedores)"
    
    def __str__(self):
        return f"{self.nomeproduto} | {self.codigobarra}"

class ProdutosClientes(models.Model):
    produtoid = models.AutoField(db_column='produtoID', primary_key=True)  # Field name made lowercase.
    nomeproduto = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    codigobarra = models.CharField(max_length=15, blank=True, null=True)
    tempoentrega = models.SmallIntegerField(blank=True, null=True)
    precorevenda = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    imagemgrande = models.FileField(max_length=100)
    imagempequena = models.FileField(max_length=100)
    descontinuado = models.SmallIntegerField(blank=True, null=True)
    fornecedorid = models.SmallIntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    categoriaid = models.SmallIntegerField(db_column='categoriaID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produtos_clientes'
        verbose_name = 'Produto do Cliente'
        verbose_name_plural  =  "Produtos Disponíveis (Clientes)"
    
    def __str__(self):
        return f"{self.nomeproduto} | {self.codigobarra}"

