#forms.py
from django.forms import ModelForm
from .models import Notedata


class NoteForm(ModelForm):
    class Meta:
        model=Notedata
        fields='__all__'
