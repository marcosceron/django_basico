from django.db import models

# Create your models here.
class ProdutoFinal(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    data = models.DateTimeField()
    horario = models.TimeField()
    validade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.categoria}"

class Temperatura(models.Model):
    temperatura = models.CharField(max_length=25)

class Ingrediente(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.CharField(max_length=100)

class Estoque(models.Model):
    produto_final = models.ForeignKey(ProdutoFinal, on_delete=models.CASCADE)

