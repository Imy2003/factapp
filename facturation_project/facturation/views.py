# facturation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from django.contrib import messages
from .models import Facture
from .forms import FactureForm






def facture_list(request):
    
    return render(request, 'facturation/facture_list.html')

def register_user(request):
    msg = None
    success = False
    form= SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
 

    return render(request, "templates/register.html", {"form": form, "msg": msg, "success": success})


def login_view(request):
   
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect ('facturation:create_facture')
        else:
            messages.info(request,'Username or password is incorrect  ')
            return redirect('/login/')
    context ={}
    return render(request, "templates/login.html", context)

def logout_view(request):
    logout(request)
    return redirect('facturation:login')

@login_required
def home(request):
    factures=Facture.objects.all()
    return render(request, 'homepage.html',{'factures':factures})


@login_required
def add_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FactureForm()
    return render(request, 'add_facture.html', {'form': form})

def add_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FournisseurForm()
    return render(request, 'add_fournisseur.html', {'form': form})


def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ServiceForm()
    return render(request, 'add_service.html', {'form': form})


def search_factures(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Perform filtering based on the query
            if query:
                factures = Facture.objects.filter(number__icontains=query)  # Example: search by facture number
            else:
                factures = Facture.objects.all()
        else:
            factures = Facture.objects.all()
            form = SearchForm()

    return render(request, 'search_factures.html', {'factures': factures, 'form': form})