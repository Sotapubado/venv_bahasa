from dataclasses import fields
from .models import Salon


class SalonCreateForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ('title', 'content', 'photo')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
