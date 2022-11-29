from django.db import models
from django.urls import reverse
from funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=70, help_text="Motivo da Hora Extra")
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    #Quando editar informações ele retorna para update_hora_extra, passando o id
    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])

    def __str__(self):
        return self.motivo
