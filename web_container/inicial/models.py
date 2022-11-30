# from django.contrib import admin
from django.db import models

# Create your models here.


class Categorias(models.Model):
    categoriaid = models.AutoField(db_column='categoriaID', primary_key=True)  # Field name made lowercase.
    nomecategoria = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"Nome da categoria: {self.nomecategoria}"


class Departamentos(models.Model):
    departamentoid = models.AutoField(db_column='departamentoID', primary_key=True)  # Field name made lowercase.
    nomedepartamento = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'departamentos'
        verbose_name = 'Departamento'
        verbose_name_plural = "Departamentos"

    def __str__(self):
        return f"Departamento: {self.nomedepartamento}"


class Estados(models.Model):
    estadoid = models.AutoField(db_column='estadoID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(max_length=20, blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'estados'
        verbose_name = 'Estado'
        verbose_name_plural = "Lista de Estados"

    def __str__(self):
        return f"Estado: {self.nome} | UF: {self.sigla}"
