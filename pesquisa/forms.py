from datetime import date
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from pesquisa.models import CustomUser


class CustomLoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.widgets.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email', 'id': 'email', 'name': 'email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Senha', 'id': 'password', 'name': 'password'}))


class RegisterForm(forms.Form):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    dt_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))

    email = forms.CharField(widget=forms.widgets.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off'}))
