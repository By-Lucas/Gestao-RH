from django.urls import path
from .views import home, logout_request, logar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('logout/', logout_request, name='sair'),
    path('logar/', logar, name='logar'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)