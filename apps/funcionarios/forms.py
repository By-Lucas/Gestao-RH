from django import forms
from .models import Funcionario

class ProfileForm(forms.ModelForm):
    funcionario_code = forms.CharField(max_length=250, label="ID da comapia", required=False)
    nome = forms.CharField(max_length=30, required=False, help_text="Opcional", label='Nome')
    sobrenome = forms.CharField(max_length=30, required=False, help_text="Opcional", label='Sobrenome')
    telefone = forms.CharField(max_length=30, required=False, help_text="Opcional", label='Número de telefone')
    email = forms.EmailField(max_length=120, help_text="Digite seu endereço de email", label='Seu email')
    foto_funcionatio = forms.ImageField(label="Avatar")
    class Meta:
        model = Funcionario
        fields = [
                'funcionario_code',
                'nome', 
                'sobrenome', 
                'telefone', 
                'email', 
                'data_nascimento',
                'departamentos', 
                'foto_funcionatio'
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['data_nascimento'].widget = forms.DateInput(format="%d/%m/%Y")

def clean_funcionario_code(self):
        id = self.data['id'] if self.data['id'] != '' else 0
        funcionario_code = self.cleaned_data['funcionario_code']
        try:
            if id > 0:
                funcionario = Funcionario.exclude(id=id).get(funcionario_code = funcionario_code)
            else:
                funcionario = Funcionario.get(funcionario_code = funcionario_code)
        except:
            return funcionario_code
        return forms.ValidationError(f"{funcionario_code} Já existe.")