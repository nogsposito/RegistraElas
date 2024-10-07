from django.shortcuts import redirect, render
from django.views import View
from .models import cadastros

class HomeView(View):
    def get (self, request):
        cadastro = cadastros.objects.all()

        ctx = {
            'todos_cadastros': cadastro,
        }

        return render(request, 'home.html', ctx)
    
class CadastrarView(View):
    def get (self, request):
        if request.method == "GET":
            return render (request, 'cadastrar.html')
        
    def post(self, request):
        if request.method == "POST":
            nome = request.POST.get('formNome')
            idade = request.POST.get('formIdade')
            cpf = request.POST.get('formCpf')
            celular = request.POST.get('formCelular')
            cep = request.POST.get('formCep')
            cidade = request.POST.get('formCidade')
            bairro = request.POST.get('formBairro')
            rua = request.POST.get('formRua')
            numero = request.POST.get('formNumero')
            complemento = request.POST.get('formComplemento')

            Cadastro = cadastros(nome = nome, idade = idade, cpf = cpf, celular = celular, cep = cep, cidade = cidade, bairro = bairro, rua = rua, numero = numero, complemento = complemento)

            Cadastro.save()

            return redirect('aplicacao:home')

class VisualizarCadastroView(View):
    def get (self, request, id):
        ctx = {'cadastro':cadastros.objects.filter(id=id).first()}

        return render (request, 'visualizar_cadastro.html', ctx)