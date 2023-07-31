# facturation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


from .models import Facture

def create_facture(request):
    
 #     if form.is_valid():
  #          form.save()   
#         return redirect('facture_list')
 #   else:
  #      form = FactureForm()
   return render(request, 'facturation/create_facture.html', {'form': form})


def facture_list(request):
    factures = Facture.objects.all()
    return render(request, 'facturation/facture_list.html', {'factures': factures})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('facture_list')  # Replace 'homepage' with the name of your homepage URL pattern
        else:
            # Add error handling for invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')
    
    

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout



def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})