from django.db import models

# Create your models here.
class cadastros(models.Model):
    nome = models.CharField(max_length=80)
    idade = models.CharField(max_length=30)
    comentarios = models.CharField(max_length=500, null=True)