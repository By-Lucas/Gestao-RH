from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json

from ..models.ponto_model import PontosQrCodeModel
from funcionarios.models import Funcionario
from funcionarios.forms import ProfileForm

def context_data():
    context = {
        'page_name' : '',
        'page_title' : 'Chat Room',
        'system_name' : 'ID do funcionario com QR Code',
        'topbar' : True,
        'footer' : True,
    }
    return context

def bate_ponto(request):
    pontos = PontosQrCodeModel.objects.all()
    nome = request.get.POST()
    if request.method == "POST":
        nome = pontos.create(nome=nome)
        messages.success(request, "Ponto batido com sucesso")

def scanner_qr(request):
    context = context_data()
    return render(request, 'ponto_qr_code/scanner_qrcode.html', context)


#@login_required
def view_scanner_bater_ponto(request):
    context = context_data()
    return render(request, 'ponto_qr_code/scanner_qr_code.html', context)

@login_required
def Bater_ponto_qrcode(request, code = None):
    pontos = PontosQrCodeModel.objects.all()
    nome = request.POST.get('nome')
    if code is None:
        return HttpResponse("O código do funcionário é inválido")
    else:
        context = context_data()
        context['funcionario'] = Funcionario.objects.get(funcionario_code=code)
        nome = pontos.create(nome=request.user.username)
        messages.success(request, "Ponto batido com sucesso")
        return render(request, 'ponto_qr_code/detalhes_qrcode.html', context)

