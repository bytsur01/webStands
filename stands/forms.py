from django.forms import ModelForm
from .models import Soldierdata


class SoldierForm(ModelForm):
    class Meta:
        model = Soldierdata
        fields = '__all__'
