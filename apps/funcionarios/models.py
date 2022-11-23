from django.db import models
from django.contrib.auth.models import User
from departamentos.models import Departamento
from empresas.models import Empresa
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image
from random import choice
import string

import uuid
import qrcode

def upload_to(instance ,filename):
    return 'user/{username}/{filename}'.format(
        username=instance.user.username, filename=filename)

def gerar_id():
    tamanho = 14
    valores = '1234567890'
    senha = ''
    for i in range(tamanho):
        senha += choice(valores)
    return senha

class Funcionario(models.Model):
    funcionario_code = models.CharField(max_length=14,default=gerar_id, editable=True, unique=True, blank=True, null=True, help_text="ID identificador QR code")
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    sobrenome = models.CharField(max_length=100, null=False, blank=False,help_text="Sobre nome do funcionario")
    telefone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=80, null=False, blank=False, help_text="E-mail")
    #Criar user junto ao cadastro(protegido) USUARIO UNICO PARA UM FUNCIONARIO
    user = models.OneToOneField(User, on_delete=models.PROTECT) 
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto_funcionatio = models.ImageField(upload_to=upload_to, default='usuario.png', null=True, blank=True)
    atualizado_em = models.DateTimeField(default=timezone.now)
    data_cadastro = models.DateTimeField(auto_now = True)

    # Apos o formulario ser validado, vai redirecionar para a pagina abaixo
    def get_absolute_url(self):
        return reverse('list_funcionarios')
    

    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'

    def __str__(self):
        #return Self.nome
        return str(f"{self.funcionario_code} - {self.nome} "+ (f"{self.sobrenome}" if not self.nome == "" else f"{self.user.username}") )
    def name(self):
        return str(f"{self.nome} "+ (f"{self.sobrenome}" if not self.nome == "" else f"{self.user.username}") )

    def save(self, *args, **kwargs):
        super(Funcionario, self).save(*args, **kwargs)
        print(self.foto_funcionatio)
        imag = Image.open(self.foto_funcionatio.path)
        if imag.width > 200 or imag.height> 200:
            output_size = (200, 200)
            imag.thumbnail(output_size)
            imag.save(self.foto_funcionatio.path)

# @receiver(post_save, sender=Funcionario)
# def create_qr(sender, instance, **kwargs):
#     code = instance.funcionario_code
#     img = qrcode.make(code)
#     instance.qr_path = img
#     print(img)
#     instance.save()

