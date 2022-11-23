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

@login_required 
def manage_employee(request, pk=None):
    context =context_data()
    if pk is None:
        context['page'] = 'add_employee'
        context['page_title'] = 'Cadastrar novo funcionário'
        context['funcionario'] = {}
    else:
        context['page'] = 'edit_employee'
        context['page_title'] = 'Atualizar funcionário'
        context['funcionario'] = Funcionario.objects.get(id=pk)

    return render(request, 'manage_employee.html', context)


@login_required
def save_funcionario(request):
    resp = { 'status' : 'failed', 'msg' : '' }
    if not request.method == 'POST':
        resp['msg'] = "Nenhum dado foi enviado para a solicitação."

    else:
        if request.POST['id'] == '':
            form = ProfileForm(request.POST, request.FILES)
        else:
            funcionario = Funcionario.objects.get(id = request.POST['id'])
            form = ProfileForm(request.POST, request.FILES, instance = funcionario)
        if form.is_valid():
            form.save()
            if request.POST['id'] == '':
                messages.success(request, f"{request.POST['employee_code']} foi adicionado com sucesso.")
            else:
                messages.success(request, f"{request.POST['employee_code']} foi atualizado com sucesso.")
            resp['status'] = 'success'
        else:
            for field in form:
                for error in field.errors:
                    if not resp['msg'] == '':
                        resp['msg'] += str("<br />")
                    resp['msg'] += str(f"[{field.label}] {error}")

    return HttpResponse(json.dumps(resp), content_type="application/json")


@login_required
def view_card(request, pk =None):
    if pk is None:
        return HttpResponse("O ID do funcionário é inválido")
    else:
        context = context_data()
        context['funcionario'] = Funcionario.objects.get(id=pk)
        return render(request, 'view_id.html', context)

@login_required
def view_details(request, code = None):
    pontos = PontosQrCodeModel.objects.all()
    nome = request.POST.get('nome')
    if code is None:
        return HttpResponse("O código do funcionário é inválido")
    else:
        context = context_data()
        context['funcionario'] = Funcionario.objects.get(funcionario_code=code)
        nome = pontos.create(nome=request.user.username)
        messages.success(request, "Ponto batido com sucesso")
        return render(request, 'view_details.html', context)


@login_required
def delete_funcionario(request, pk=None):
    resp = { 'status' : 'failed', 'msg' : '' }
    if pk is None:
        resp['msg'] = "Nenhum dado foi enviado para a solicitação."
    else:
        try:
            Funcionario.objects.get(id=pk).delete()
            resp['status'] = 'success'
            messages.success(request, 'O funcionário foi excluído com sucesso.')
        except:
            resp['msg'] = "O funcionário falhou ao excluir."

    return HttpResponse(json.dumps(resp), content_type="application/json")