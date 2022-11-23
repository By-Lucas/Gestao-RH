from django.db import models
from funcionarios.models import Funcionario
from django.shortcuts import reverse

class Documento(models.Model):
    descricao = models.CharField(max_length=70, help_text="Descrição do documento")
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos/', null=True, blank=True)

    # Redireciona para pagina de ediar de onde o usuario pertence
    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.pertence.id])

    def __str__(self):
        return self.descricao
