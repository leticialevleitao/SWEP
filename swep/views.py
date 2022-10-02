from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def nome(request):
    return render(request, 'nome.html', {'nome': 'SWEP'})

def alimentos(request): 
    return render(request, 'SWEP_HTML/SWEP.html')