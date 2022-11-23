from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import (
            ListView, UpdateView,
            DeleteView, CreateView
            )
from .models import Funcionario
from .forms import ProfileForm
from django.urls import reverse_lazy

class FuncionariosList(ListView):
    model = Funcionario
    # Cada empresa verá apenas seus funcionários
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionariosEdit(UpdateView):
    model = Funcionario
    fields=['nome', 'sobrenome', 
            'telefone', 'email', 
            'departamentos', 'foto_funcionatio']

class FuncionariosDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionariosCreate(CreateView):
    template_name = 'funcionarios/funcionario_register.html'
    model = Funcionario
    fields=['nome', 'sobrenome', 
            'telefone', 'email', 
            'departamentos', 'foto_funcionatio']

    def form_valid(self, form):
        #Enviar o commit mas nao salvar no banco ate ser feito algumas coisas antes
        funcionario = form.save(commit=False)
        # Cria um usuario com nome e sobrenome junto
        username = funcionario.nome.split(' ')[0] + funcionario.sobrenome.split(' ')[0]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionariosCreate, self).form_valid(form)