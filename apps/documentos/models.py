from django.db import models
from funcionarios.models import Funcionario

class Documento(models.Model):
    descricao = models.CharField(max_length=70, help_text="Descrição do documento")
    proprietario_documento = models.ForeignKey(Funcionario, on_delete=models.PROTECT)


    
    def __str__(self):
        return self.descricao
