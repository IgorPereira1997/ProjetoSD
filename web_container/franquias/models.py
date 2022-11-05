from django.db import models

# Create your models here.


class Franquias(models.Model):
    franquiaid = models.AutoField(db_column='franquiaID', primary_key=True)  # Field name made lowercase.
    nomegerente = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estadoid = models.IntegerField(db_column='estadoID')  # Field name made lowercase.
    telefone = models.CharField(max_length=15, blank=True, null=True)
    dataabertura = models.DateField()
    faturamento = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'franquias'
