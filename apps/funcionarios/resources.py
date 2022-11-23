from import_export import resources
from .models import Funcionario

class FuncionarioResource(resources.ModelResource):
    class Meta:
        model = Funcionario