from django.db import models
from map_alert import settings
from asgiref.sync import async_to_sync


class Tipo(models.Model):
    nome = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nome


class LocalUnifap(models.Model):
    nome = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.nome


class Alert(models.Model):
    NAO_RESOLVIDO = 0
    RESOLVIDO = 1
    NAO_SERA_RESOLVIDO = 2

    STATUS_CHOICES = (
        (NAO_RESOLVIDO, 'Não Resolvido'),
        (RESOLVIDO, 'Resolvido'),
        (NAO_SERA_RESOLVIDO, 'Não será resolvido')
    )

    VISIVEL = 1
    NAO_VISIVEL = 0
    VISIBILIDADE = (
        (VISIVEL, 'Está Visível'),
        (NAO_VISIVEL, 'Não está visível')
    )

    latitude = models.FloatField()
    longitude = models.FloatField()
    local = models.ForeignKey(LocalUnifap, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=140)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=0)
    prazo = models.DateField(auto_now=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE)
    image = models.FileField()

    def __str__(self):
        return str(f"(Local: {self.local}, Tipo: {self.tipo})")
