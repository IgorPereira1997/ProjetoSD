from django.db import models

# Create your models here.

class Clientes(models.Model):
    clienteid = models.AutoField(db_column='clienteID', primary_key=True)  # Field name made lowercase.
    nomecompleto = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    numero = models.CharField(max_length=15, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    ddd = models.CharField(max_length=3, blank=True, null=True)
    telefone = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.CharField(max_length=10, blank=True, null=True)
    senha = models.CharField(max_length=10, blank=True, null=True)
    nivel = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'clientes'

    def __str__(self):
        return self.nomecompleto + ' | '+ self.email

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
    
    def __str__(self):
        return self.nomefornecedor


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

    def __str__(self):
        return self.nome + " | " + self.email