from django.db.models import TextField

from .models import Vessels, Person, Type
from django import forms
from django.forms import ModelForm, CharField, PasswordInput, TextInput, MultipleChoiceField, IntegerField, \
    CheckboxSelectMultiple, ModelChoiceField, ModelMultipleChoiceField


class Entry(ModelForm):
    login = CharField(widget=TextInput(attrs={'size': '40'}), required=True)
    password = CharField(widget=PasswordInput(attrs={'size': '37'}), required=True, )

    class Meta:
        model = Person
        fields = ['login', 'password']


class FindVessel(forms.Form):
    find_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название',
                                                              "name": "find_name"}), label='', required=False)

    IMO = forms.IntegerField(
        widget=forms.NumberInput(attrs={'type': 'number', 'placeholder': 'IMO', 'max_value': '9999999',
                                        'min': '0', 'size': '40'}), label='', required=False)


class FilterVessel(ModelForm):
    name = CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}), label='', required=False)
    IMO = IntegerField(widget=forms.NumberInput(attrs={'type': 'number', 'placeholder': 'IMO', 'max_value': '9999999',
                                                       'min': '0', 'size': '40'}), label='', required=False)



    class Meta:
        model = Vessels
        fields = ['name', 'IMO']
