from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View

from .models import cadastros

class CadastrosView(View):
    def get (self, request):
        cadastro = cadastros.objects.all()

        ctx = {
            'todos_cadastros': cadastro,
        }

        return render(request, 'home.html', ctx)

class CadastroDetalhadoView(View):

    def get (self, request, id):
        ctx = {'cadastro':cadastros.objects.filter(id=id).first()}
        return render (request, 'visualizar_cadastro.html', ctx)
    
