
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import (
                    FuncionariosList, 
                    FuncionariosEdit, 
                    FuncionariosDelete, 
                    FuncionariosCreate
                    )


urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>/', FuncionariosEdit.as_view(), name='update_funcionario'),
    path('deletar/<int:pk>/', FuncionariosDelete.as_view(), name='delete_funcionario'),
    path('cadastrar-funcionario/', FuncionariosCreate.as_view(), name='create_funcionario'),
]

# Para carregar STATIC e as MIDIAS
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)