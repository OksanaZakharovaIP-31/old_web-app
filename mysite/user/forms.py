from django.db.models import TextField
from django.core.validators import RegexValidator
from .models import Vessels, Person, Type
from django import forms
from django.forms import ModelForm, CharField, PasswordInput, TextInput, MultipleChoiceField, IntegerField, \
    CheckboxSelectMultiple, ModelChoiceField, ModelMultipleChoiceField, FileField

AlphaValidator = RegexValidator(r'^[а-яА-я]*$', 'Only alpha characters are allowed.')
EnglishNameValidator = RegexValidator(r'^[A-Z_]*$', 'Only alpha without space characters are allowed.')


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


class AddType(ModelForm):
    type = CharField(widget=forms.TextInput(attrs={'placeholder': 'Вид'}), validators=[AlphaValidator], label='')

    class Meta:
        model = Type
        fields = ['type']


class AddVessel(ModelForm):
    class Meta:
        model = Vessels
        fields = ['name', 'type', 'IMO', 'name_in_en', 'user']
        labels = {
            'user': 'Пользователь',
            'name': '',
            'type': 'Тип',
            'IMO': '',
            'name_in_en': '',
            'photo': 'Фотография'
        }
        widgets = {
            # 'user': ModelChoiceField(queryset=Person.objects.all(), attrs={'placeholder': 'Пользователь'}),
            'name': TextInput(attrs={'placeholder': 'Название'}),
            'IMO': forms.NumberInput(attrs={'type': 'number', 'placeholder': 'IMO', 'max_value': '9999999',
                                            'min': '1000000'}),
            'name_in_en': TextInput(attrs={'placeholder': 'Название на английском',
                                           'title': "Название на английском языке, только большими буквами, пробелы "
                                                    "заменить нижним подчеркиванием", }),
            # 'type': 'Тип',
            # 'IMO': '',
            # 'name_in_en': '',
            # 'photo': forms.ImageField()
        }
        validators = {
            'name_in_en': [EnglishNameValidator]
        }
        required = {
            'photo': False}
