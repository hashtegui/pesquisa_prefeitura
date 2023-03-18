from django.http import HttpRequest
from django.shortcuts import render, redirect
from .forms import FormPessoa

# Create your views here.


def index(request: HttpRequest):
    return render(request, 'pesquisa/index.html', )
