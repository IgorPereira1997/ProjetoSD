from django.db import models

# Create your models here.

class Transportadoras(models.Model):
    transportadoraid = models.AutoField(db_column='transportadoraID', primary_key=True)  # Field name made lowercase.
    nometransportadora = models.CharField(max_length=50, blank=True, null=True)
    endereco = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    cidade = models.CharField(max_length=50, blank=True, null=True)
    estadoid = models.IntegerField(db_column='estadoID', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(max_length=10, blank=True, null=True)
    cnpj = models.CharField(max_length=19, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'transportadoras'

    def __str__(self):
        return (self.transportadoraid + ' ' +
                self.nometransportadora + ' ' +
                self.endereco + ' ' +
                self.telefone + ' ' +
                self.cidade + ' ' +
                self.estadoid + ' ' +
                self.cep + ' ' +
                self.cnpj)