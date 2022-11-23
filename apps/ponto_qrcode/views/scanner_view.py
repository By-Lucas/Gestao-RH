from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def context_data():
    context = {
        'page_name' : '',
        'page_title' : 'Chat Room',
        'system_name' : 'ID do funcionario com QR Code',
        'topbar' : True,
        'footer' : True,
    }
    return context


#@login_required
def view_scanner(request):
    context = context_data()
    return render(request, 'scanner.html', context)