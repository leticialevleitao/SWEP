from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm

# Create your views here. - Criar as Views de cada página.
def IndexView(request):
    return render(request, 'landing.html')

def RegisterView(request):
    if request.method == 'GET':
        form  = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('index')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            
        return render(request, 'register.html', context)
    
    return render(request, 'register.html', {})