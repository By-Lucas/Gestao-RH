from django.db import models

class Departamento(models.Model):
    departamento = models.CharField(max_length=100, help_text="Nome do departamento")

    def __str__(self):
        return self.departamento