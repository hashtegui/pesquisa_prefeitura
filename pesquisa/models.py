from django.db import models

# Create your models here.


class Pessoa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=12)
