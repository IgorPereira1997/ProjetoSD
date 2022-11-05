from ProjetoSD_2 import settings
import os
from django.db import models
from django.utils.safestring import mark_safe
from listar_produtos.models import Produtos
from login.models import Clientes
from listar_transportadoras.models import Transportadoras
# Create your models here.


class Pedidos(models.Model):
    pedidoid = models.AutoField(db_column='pedidoID',
                                primary_key=True)
    clienteid = models.IntegerField(db_column='clienteID')
    transportadoraid = models.IntegerField(db_column='transportadoraID',
                                           blank=True,
                                           null=True)
    data_pedido = models.DateField()
    data_saida = models.DateField(blank=True,
                                  null=True)
    data_entrega = models.DateField(blank=True,
                                    null=True)
    status_pedido = models.SmallIntegerField()
    valor_pedido = models.DecimalField(max_digits=10,
                                       decimal_places=2)
    conhecimento = models.CharField(max_length=20,
                                    blank=True,
                                    null=True)

    class Meta:
        managed = True
        db_table = 'pedidos'
        ordering = ('pedidoid', 'data_pedido', 'status_pedido', 'valor_pedido')
        verbose_name = 'Pedido'
        verbose_name_plural = "Pedidos"

    def cliente_tag(self):
        try:
            cli = Clientes.objects.get(clienteid=self.clienteid)
            return cli.nomecompleto
        except (cli is None):
            return "Cliente não mais associado"

    def transportadora_tag(self):
        try:
            transp = Transportadoras.objects.get(
                transportadoraid=self.transportadoraid
            )
            return transp.nometransportadora
        except (transp is None):
            return "Transportadora não mais associada"

    def valor(self):
        return "R$ " + str(self.valor_pedido).replace('.', ',')

    def status_tag(self):
        status = PedidosStatus.objects.get(statusid=self.status_pedido)
        return status.nomestatus

    def __str__(self):
        nome = PedidosStatus.objects.get(statusid=self.status_pedido)
        return "Data do Pedido: {} | Status: {} | Valor: {}".format(self.data_pedido,
                                                                    nome.nomestatus,
                                                                    self.valor)


class PedidosItem(models.Model):
    pedidoid = models.IntegerField(
        db_column='pedidoID',
        blank=True,
        null=True)
    produtoid = models.IntegerField(db_column='produtoID',
                                    blank=True,
                                    null=True)
    precounitario = models.DecimalField(max_digits=10,
                                        decimal_places=2,
                                        blank=True,
                                        null=True)
    quantidade = models.SmallIntegerField(blank=True,
                                          null=True)

    class Meta:
        managed = True
        db_table = 'pedidos_item'
        verbose_name = 'Item do Pedido'
        verbose_name_plural = "Items dos Pedidos"

    def produto_tag(self):
        try:
            produto = Produtos.objects.get(produtoid=self.produtoid)
            return produto.nomeproduto
        except (produto is None):
            return "Nome do Produto indisponível"

    def image_tag(self):
        try:
            imagem = Produtos.objects.get(produtoid=self.produtoid)
            return mark_safe('<img src="{}"/>'.format(
                os.path.join(settings.MEDIA_LINK, str(imagem.imagempequena))))
        except imagem.DoesNotExist:
            return 'Imagem indisponível'
    image_tag.short_description = 'Image'

    def quantidade_str(self):
        if self.quantidade > 1:
            return str(self.quantidade) + " unidades"
        else:
            return str(self.quantidade) + " unidade"

    def precounitario_tag(self):
        return "R$ " + str(self.precounitario).replace('.', ',')

    def __str__(self):
        return "Número do Pedido: {} | Produto: {} | QTD: {}".format(self.pedidoid, self.produto_tag, self.quantidade)


class PedidosStatus(models.Model):
    statusid = models.AutoField(db_column='statusID',
                                primary_key=True)
    nomestatus = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'pedidos_status'
        verbose_name = 'Status do Pedido'
        verbose_name_plural = "Status dos Pedidos"

    def __str__(self):
        return f"ID: {self.statusid} | Status: {self.nomestatus}"
