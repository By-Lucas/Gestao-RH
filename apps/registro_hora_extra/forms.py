from django import forms
from funcionarios.models import Funcionario
from .models import RegistroHoraExtra

class HoraExtraForm(forms.ModelForm):
    # Só vai filtar hora extra do funcionario que faz parte da empresa
    # funcionarios que faz parte de outra empresa não vai mostrar
    def __init__(self, user, *args, **kwargs):
        super(HoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        )
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas', 'utilizada']