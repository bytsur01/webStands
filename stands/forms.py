from typing import Type

from django.forms import ModelForm
from .models import *


class SoldierForm(ModelForm):
    class Meta:
        model = Soldierdata
        fields = '__all__'


class IccTableOneForm(ModelForm):
    class Meta:
        model = IccTableOne
        fields = '__all__'


class IccTableTwoForm(ModelForm):
    class Meta:
        model = IccTableTwo
        fields = '__all__'


class IccTableThreeForm(ModelForm):
    class Meta:
        model = IccTableThree
        fields = '__all__'


class IccTableFourForm(ModelForm):
    class Meta:
        model = IccTableFour
        fields = '__all__'
