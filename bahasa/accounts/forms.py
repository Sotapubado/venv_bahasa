from dataclasses import fields
from importlib.metadata import MetadataPathFinder

from .models import Account
from django import forms


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('introduction', 'icon')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
           field.widget.attrs['class']='form-control'

