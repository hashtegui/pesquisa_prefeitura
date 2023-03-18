from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import FormPessoa

# Create your views here.


def index(request: HttpRequest):

    if request.method == 'POST':
        form = FormPessoa(request.POST)
        if form.is_valid():
            return redirect('/')
    else:

        form = FormPessoa()
    return render(request, 'base.html', {'form': form})
