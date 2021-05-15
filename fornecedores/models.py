from django.db import models

# Create your models here.

class Fornecedores(models.Model):
    fornecedorid = models.AutoField(db_column='fornecedorID', primary_key=True)  # Field name made lowercase.
    nomefornecedor = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    ddd = models.IntegerField(blank=True, null=True)
    telefone = models.CharField(max_length=14, blank=True, null=True)
    usuario = models.CharField(max_length=20, blank=True, null=True)
    senha = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'fornecedores'


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