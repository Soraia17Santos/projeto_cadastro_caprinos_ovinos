from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    cobertura = models.IntegerField()
    raca = models.TextField(max_length=255)
    brinco = models.TextField(max_length=255)
    idade = models.ImageField()
    data = models.IntegerField()
    reprodutor = models.TextField(max_length=255)
    peso = models.IntegerField()
    ecc = models.IntegerField()
    tipo_acasalamento = models.IntegerField()
    tipo_estro = models.IntegerField()
    