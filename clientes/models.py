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
        return self.usuario + ' '+ self.senha