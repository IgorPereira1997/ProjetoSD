from django.db import models
from inicial.models import Departamentos, Estados
# Create your models here.


class Clientes(models.Model):
    clienteid = models.AutoField(db_column='clienteID', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(max_length=150, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    estadoid = models.SmallIntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clientes'
        verbose_name = 'Cliente'
        verbose_name_plural = "Lista de Clientes"

    def estado_tag(self):
        estado = Estados.objects.get(estadoid=self.estadoid)
        return estado.sigla

    def __str__(self):
        return "Nome: " + self.nomecompleto + ' | Email: ' + self.email


class Fornecedores(models.Model):
    fornecedorid = models.AutoField(db_column='fornecedorID', primary_key=True)  # Field name made lowercase.
    nomefornecedor = models.CharField(max_length=150, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    estadoid = models.SmallIntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    ddd = models.SmallIntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    usuario = models.CharField(max_length=100, blank=True, null=True)
    senha = models.CharField(max_length=100, blank=True, null=True)
    cep = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fornecedores'
        verbose_name = 'Fornecedor'
        verbose_name_plural = "Lista de Fornecedores"

    def estado_tag(self):
        estado = Estados.objects.get(estadoid=self.estadoid)
        return estado.sigla

    def __str__(self):
        return "Nome do Fornecedor: " + self.nomefornecedor + " | Email: " + self.email


class FornecedoresContatos(models.Model):
    contatoid = models.AutoField(db_column='contatoID', primary_key=True)  # Field name made lowercase.
    fornecedorid = models.IntegerField(db_column='fornecedorID', blank=True, null=True)  # Field name made lowercase.
    departamentoid = models.IntegerField(db_column='departamentoID', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fornecedores_contatos'
        verbose_name = 'Contato do Fornecedor'
        verbose_name_plural = "Contatos dos Fornecedores"

    def empresa(self):
        forn = Fornecedores.objects.get(fornecedorid=self.fornecedorid)
        return forn.nomefornecedor

    def departamento(self):
        dep = Departamentos.objects.get(departamentoid=self.departamentoid)
        return dep.nomedepartamento

    def __str__(self):
        return "Nome do Funcionário: " + self.nome + " | Empresa: " + self.empresa + " | Email: " + self.email
