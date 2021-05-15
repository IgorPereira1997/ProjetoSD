from django.db import models

# Create your models here.

class Pedidos(models.Model):
    pedidoid = models.AutoField(db_column='pedidoID', primary_key=True)  # Field name made lowercase.
    clienteid = models.IntegerField(db_column='clienteID')  # Field name made lowercase.
    transportadoraid = models.IntegerField(db_column='transportadoraID', blank=True, null=True)  # Field name made lowercase.
    data_pedido = models.DateField()
    data_saida = models.DateField(blank=True, null=True)
    data_entrega = models.DateField(blank=True, null=True)
    status_pedido = models.IntegerField()
    valor_pedido = models.DecimalField(max_digits=10, decimal_places=2)
    conhecimento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos'


class PedidosItem(models.Model):
    pedidoid = models.IntegerField(db_column='pedidoID', blank=True, null=True)  # Field name made lowercase.
    produtoid = models.IntegerField(db_column='produtoID', blank=True, null=True)  # Field name made lowercase.
    precounitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    quantidade = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'pedidos_item'


class PedidosStatus(models.Model):
    statusid = models.AutoField(db_column='statusID', primary_key=True)  # Field name made lowercase.
    nomestatus = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pedidos_status'