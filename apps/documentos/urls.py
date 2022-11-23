from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import DocumentoCreate, DocumentoDelete

urlpatterns = [
    path('novo/<int:funcionario_id>/',DocumentoCreate.as_view(), name='create_documento'),
    path('delete/',DocumentoDelete.as_view(), name='delete_documento'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)