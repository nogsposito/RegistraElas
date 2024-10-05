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
    
class AdicionarCadastro(View):
    def get (self, request):
        if request.method == "GET":
            return render (request, 'adicionar_cadastro.html')
        
    def post(self, request):
        if request.method == "POST":
            nome = request.POST.get('formNome')
            idade = request.POST.get('formIdade')

            Cadastro = cadastros(nome = nome, idade = idade)

            Cadastro.save()

            return redirect('aplicacao:home')