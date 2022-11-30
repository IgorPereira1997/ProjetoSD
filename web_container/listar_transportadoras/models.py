from inicial.models import Estados
from django.db import models

# Create your models here.


class Transportadoras(models.Model):
    transportadoraid = models.AutoField(db_column='transportadoraID', primary_key=True)  # Field name made lowercase.
    nometransportadora = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=150, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=150, blank=True, null=True)
    estadoid = models.SmallIntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    cnpj = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transportadoras'
        verbose_name = 'Transportadora'
        verbose_name_plural = "Transportadoras Disponíveis"

    def estado_tag(self):
        estado = Estados.objects.get(estadoid=self.estadoid)
        return estado.sigla

    def __str__(self):
        return f"Nome da Transportadora: {self.nometransportadora} | CNPJ: {self.cnpj}"
