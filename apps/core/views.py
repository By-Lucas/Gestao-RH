from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth

# Alertas de messagens
from django.contrib import messages
from django.contrib.messages import constants

from funcionarios.models import Funcionario

#@login_required
def home(request):
    #Pegas informacoes do usuario
    data = {}
    data['usuario'] =  request.user

    return render(request, "core/index.html", data)

def logar(request):
    if request.method == 'GET':
        # Se o ususario já estiver logado, será direcionado para pagina principal
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'core/index.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('password')

        # existe um usuario e senha igual o que foi digitado?
        usuario = auth.authenticate(username=username, password=senha)
        if not usuario:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha incorreta!')
            return redirect('view_scanner_bater_ponto')
        else:
            auth.login(request, usuario) #logar e ser redirecionado para a raiz do sistema
            messages.add_message(request, constants.SUCCESS, f'Usuário "{request.user.username}" logado com suacesso!')
            return redirect('/')
            
def logout_request(request):
    logout(request)
    return redirect("home")
