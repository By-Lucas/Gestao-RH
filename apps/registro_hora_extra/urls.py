from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    HoraExtraList, HoraExtraUpdate,
    HoraExtraDelete, HoraExtraCreate
    )

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_horas_extra'),
    path('cadastrar/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('editar/<int:pk>', HoraExtraUpdate.as_view(), name='update_hora_extra'),
    path('delete/<int:pk>', HoraExtraDelete.as_view(), name='delete_hora_extra'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)