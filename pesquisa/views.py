from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from xhtml2pdf import pisa

from .forms import CustomLoginForm, RegisterForm
from .models import CustomUser

# Create your views here.


def index(request: HttpRequest):
    return render(request, 'index.html', )


def login_function(request: HttpRequest):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = CustomUser.objects.get(email=email)
        if user is not None:
            login(request, user=user)
            return redirect('pagina_inicial')
        else:
            print('Erro fazer login')

    form = CustomLoginForm()
    return render(request, 'user/login.html', {'form': form})


def register(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data.get('email')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            password = form.cleaned_data.get('password1')
            dt_nascimento = form.cleaned_data.get('dt_nascimento')
            cpf = form.cleaned_data.get('cpf')

            user = CustomUser(first_name=first_name, last_name=last_name,
                              dt_nascimento=dt_nascimento, cpf=cpf, password=password, email=email)

            user.save()
            return redirect(request, 'login')
        else:
            return render(request, 'index.html')
    else:
        form = RegisterForm()
        return render(request, 'user/register.html', {'form': form})


@login_required(login_url='/login')
def pagina_inicial(request: HttpRequest):
    return render(request, 'user/logado/index.html')


def generate_pdf(request: HttpRequest):
    html = render(request, 'user/logado/index.html', {}).content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="arquivo.pdf"'

    # Converte o conteúdo HTML em PDF usando a biblioteca xhtml2pdf
    pisa.CreatePDF(html, dest=response)

    return response
