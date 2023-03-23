from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm, RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request: HttpRequest):
    return render(request, 'index.html', )


def login_function(request: HttpRequest):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            return redirect('pagina_inicial')
        else:
            print('Erro fazer login')

    form = CustomLoginForm()
    return render(request, 'user/login.html', {'form': form})


def register(request):
    form = RegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required(login_url='/login')
def pagina_inicial(request: HttpRequest):
    return render(request, 'user/logado/index.html')
