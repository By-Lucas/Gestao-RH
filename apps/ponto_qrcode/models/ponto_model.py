from django.db import models
from funcionarios.models import Funcionario
from django.utils import timezone
from datetime import datetime

def data_atual():
    agora = datetime.now()
    agora_str = agora.strftime("%A %d %B, %y  %H:%M")
    return agora_str

class diasModel(models.Model):
    dias = models.DateTimeField()


class PontosQrCodeModel(models.Model):
    nome = models.CharField(max_length=20, null=True, blank=True)
    dia = models.CharField(max_length=20, default=data_atual, null=True, blank=True)
    #funcionario_qr = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    hora_do_ponto = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id} : {self.nome}"