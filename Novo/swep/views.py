from django.shortcuts import render
from django.shortcuts import render, redirect
import requests

# Create your views here.
def paginainicial(request):
    return render(request, 'paginainicial/paginainicial.html')

def alimentos(request): 
    return render(request, 'alimentos/alimentos.html')

def login(request): 
    return render(request, 'login/login.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        usuario = request.POST['usuario']
        regiao = request.POST['regiao']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']

        user_data ={
                        "nome": nome,
                        "usuario": usuario,
                        "email": email,
                        "senha": senha,
                        "regiao": regiao
                    }

        register_url = 'http://127.0.0.1:8000/bancouser/'
        result = requests.post(register_url, data=user_data)

        return redirect('login')

    else:
        return render(request, 'cadastro/cadastro.html')


def indicacoes(request):
    if request.method == 'POST':
        tipo = request.POST['tipo']
        descricao2 = request.POST['descricao2']

        indicacoes_data ={
                        "descricao2": descricao2,
                        "tipo": tipo,
                    }

        register_url = 'http://127.0.0.1:8000/bancoindicacoes/'
        result = requests.post(register_url, data=indicacoes_data)

        return redirect('')

    else:
        return render(request, 'indicacoes/indicacoes.html')

def receitas(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        ingredientes = request.POST['ingredientes']
        descricao = request.POST['description']

        receitas_data ={
                        "titulo": titulo,
                        "ingredientes": ingredientes,
                        "descricao": descricao,
                    }

        register_url = 'http://127.0.0.1:8000/bancoreceitas/'
        result = requests.post(register_url, data=receitas_data)

        return redirect('')

    else:
        return render(request, 'receitas/receitas.html')


