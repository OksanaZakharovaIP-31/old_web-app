from django.db.models import TextField

from .models import Vessels, Person
from django.forms import ModelForm, CharField, PasswordInput, TextInput

'''class AddForm(ModelForm):
    class Meta:
        model = Vessels
        fields = ['name', 'IMO', 'type', 'photo', 'user']'''

class Entry(ModelForm):
    login = CharField(widget=TextInput(attrs={'size':'40'}),required=True)
    password = CharField(widget=PasswordInput(attrs={'size':'37'}), required=True,)
    class Meta:
        model = Person
        fields = ['login', 'password']


