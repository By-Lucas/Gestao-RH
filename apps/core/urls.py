
from django.urls import path
from .views import home, logout_request

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_request, name='sair'),
]
