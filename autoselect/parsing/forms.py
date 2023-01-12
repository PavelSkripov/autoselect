from django import forms
from .models import *

class AddForm(forms.Form):
    marking = forms.CharField(max_length=120, label="Введите маркировку:", widget=forms.TextInput(attrs={'class': 'form-input'}))