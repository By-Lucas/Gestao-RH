from import_export import resources
from .models import Departamento

class Departamento_Resource(resources.ModelResource):
    class Meta:
        model = Departamento
        fields = ['departamento', 'empresa']