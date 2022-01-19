from select import select
from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")

    def __str__(Self):
        return Self.nome