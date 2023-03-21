from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from django.shortcuts import render, redirect


# Create your views here.


def index(request: HttpRequest):
    return render(request, 'index.html', )


def login_function(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None:
                login(request, user=user)
                render(request, 'user/login/index.html')
            else:
                form.add_error(None, 'Usuário e/ou senha incorretos')
        else:
            print(form.errors)
            print('Formulário não é válido')
    else:
        form = CustomLoginForm()
    return render(request, 'user/login.html', {'form': form})


def register(request):
    return render(request, 'user/register.html')
