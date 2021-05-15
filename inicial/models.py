from django.db import models

# Create your models here.

class Categorias(models.Model):
    categoriaid = models.AutoField(db_column='categoriaID', primary_key=True)  # Field name made lowercase.
    nomecategoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorias'

class Departamentos(models.Model):
    departamentoid = models.AutoField(db_column='departamentoID', primary_key=True)  # Field name made lowercase.
    nomedepartamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamentos'

class Estados(models.Model):
    estadoid = models.AutoField(db_column='estadoID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=20, blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'estados'