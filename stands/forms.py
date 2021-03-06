from typing import Type

from django.forms import ModelForm
from .models import *


class SoldierForm(ModelForm):
    class Meta:
        model = Soldierdata
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SoldierForm, self).__init__(*args, **kwargs)
        self.fields['DODID'].widget.attrs[
            'class'] = 'form-control'
        self.fields['last_name'].widget.attrs[
            'class'] = 'form-control'
        self.fields['MOS'].widget.attrs[
            'class'] = 'form-control'
        self.fields['Battery'].widget.attrs[
            'class'] = 'form-control'
        self.fields['first_name'].widget.attrs[
            'class'] = 'form-control'

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
