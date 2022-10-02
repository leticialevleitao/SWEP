from django.shortcuts import render
from django.shortcuts import render, redirect
import requests

# Create your views here.
def nome(request):
    return render(request, 'nome.html', {'nome': 'SWEP'})

def alimentos(request): 
    return render(request, 'SWEP_HTML/SWEP.html')

def login(request): 
    return render(request, 'login/login.html')

def cadastro(request):
    if request.method == 'POST':
        name = request.POST['nome']
        email = request.POST['email']
        nickname = request.POST['nickname']
        region = request.POST['regiao']
        password = request.POST['password']
        password2 = request.POST['password2']

        user_data ={
                        "name": name,
                        "nick_name": nickname,
                        "email": email,
                        "password": password,
                        "region": region
                    }

        register_url = 'http://127.0.0.1:8000/user/'
        result = requests.post(register_url, data=user_data)

        return redirect('login')

    else:
        return render(request, 'cadastro/cadastro.html')

