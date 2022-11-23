from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from .views.ponto_qrcode import view_scanner_bater_ponto, Bater_ponto_qrcode, scanner_qr
from .views.scanner_view import view_scanner
from .views.save_funcionario import save_funcionario, view_card, view_details, manage_employee, delete_funcionario

urlpatterns = [
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),

    path('edit_employee/<int:pk>',manage_employee,name='edit-employee'),
    path('delete/<int:pk>',delete_funcionario,name='deletar_funcionario'),

    path('view_card/<int:pk>',view_card, name='view-card'),
    path('view_details/<str:code>',view_details, name='view-details'),
    path('view_details',view_details, name='scanned-code'),
    path('salvar-funcionario',save_funcionario, name='save-employee'),
    path('scanner/',view_scanner, name='view-scanner'),

    # Parte QR Code 
    path('scanner-qr/',view_scanner_bater_ponto, name='view_scanner_bater_ponto'),
    path('scanner-detalhes/<str:code>/',Bater_ponto_qrcode, name='scanner_qrcode'),
    path('scanner-detalhes',Bater_ponto_qrcode, name='Bater_ponto_qrcode'),
    path('scanner-qrcode/',scanner_qr, name='scanner_qr'),


]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)