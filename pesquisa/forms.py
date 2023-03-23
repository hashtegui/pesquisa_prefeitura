from django import forms
from django.contrib.auth.forms import AuthenticationForm

from pesquisa.models import CustomUser


class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.widgets.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email', 'name': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha', 'id': 'password', 'name': 'password'}))


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'cpf']
