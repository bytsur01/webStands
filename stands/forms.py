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
        self.fields['Battery'].widget.attrs[
            'class'] = 'form-control'
        self.fields['Rank'].widget.attrs[
            'class'] = 'form-control'
        self.fields['Platoon'].widget.attrs[
            'class'] = 'form-control'
        self.fields['Battalion'].widget.attrs[
            'class'] = 'form-control'
        self.fields['Position'].widget.attrs[
            'class'] = 'form-control'


class CrgTableOneForm(ModelForm):
    class Meta:
        model = CrgTableOne
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CrgTableOneForm, self).__init__(*args, **kwargs)
        self.fields['soldier'].widget.attrs[
            'class'] = 'form-control'
        self.fields['t_1_tasks'].widget.attrs[
            'class'] = 'form-control'
        self.fields['task_complete'].widget.attrs[
            'class'] = 'form-control'
        self.fields['date_completed'].widget.attrs[
            'class'] = 'form-control'
        self.fields['trainer'].widget.attrs[
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
