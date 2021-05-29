from django.db import models
from listar_produtos.models import Produtos
# Create your models here.

class Pedidos(models.Model):
    pedidoid = models.AutoField(db_column='pedidoID', primary_key=True)  # Field name made lowercase.
    clienteid = models.IntegerField(db_column='clienteID')  # Field name made lowercase.
    transportadoraid = models.IntegerField(db_column='transportadoraID', blank=True, null=True)  # Field name made lowercase.
    data_pedido = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    status_pedido = models.SmallIntegerField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    conhecimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos'
        ordering = ('pedidoid', 'data_pedido', 'status_pedido', 'valor_pedido')
        verbose_name = 'Pedido'
        verbose_name_plural  =  "Pedidos"

    def __str__(self):
        return f"{self.data_pedido} | Status:{self.status_pedido} | Valor: {self.valor_pedido}"


class PedidosItem(models.Model):
    pedidoid = models.IntegerField(db_column='pedidoID', blank=True, null=True)  # Field name made lowercase.
    produtoid = models.IntegerField(db_column='produtoID', blank=True, null=True)  # Field name made lowercase.
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos_item'
        verbose_name = 'Item do Pedido'
        verbose_name_plural  =  "Items dos Pedidos"  

    def __str__(self):
        return f"{self.pedidoid} | {Produtos.objects.filter(produtoid__exact=self.produtoid).values('nomeproduto')} | QTD: {self.quantidade}"



class PedidosStatus(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    nomestatus = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pedidos_status'
        verbose_name = 'Status do Pedido'
        verbose_name_plural  =  "Status dos Pedidos"

    def __str__(self):
        return f"ID: {self.statusid} | {self.nomestatus}"