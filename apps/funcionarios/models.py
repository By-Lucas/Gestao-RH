from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    #Criar user junto ao cadastro(protejido) USUARIO UNICO PARA UM FUNCIONARIO
    user = models.OneToOneField(User, on_delete=models.PROTECT) 
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)



    def __str__(Self):
        return Self.nome