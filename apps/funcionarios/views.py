from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "funcionarios.html")