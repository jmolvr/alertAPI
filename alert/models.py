from django.db import models


class Tipo(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome


class LocalUnifap(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nome


class Alert(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    local = models.ForeignKey(LocalUnifap, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=140)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"(Local: {self.local}, Tipo: {self.tipo})")
