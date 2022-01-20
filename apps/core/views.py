from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "core/index.html")

def logout_request(request):
    logout(request)
    return redirect("home")