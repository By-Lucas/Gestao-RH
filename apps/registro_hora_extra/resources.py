from import_export import resources
from .models import RegistroHoraExtra


class HoraExtraResource(resources.ModelResource):
    class Meta:
        model = RegistroHoraExtra