import django_tables2 as tables
from .models import Soldierdata


class Soldiertable(tables.Table):
    class Meta:
        model = Soldierdata
        template_name = 'django_tables2/bootstrap.html'
