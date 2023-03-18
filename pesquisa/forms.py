from django import forms
from .models import Pessoa


class FormPessoa(forms.Form):
    nome = forms.CharField(label='Seu nome', max_length=100)
