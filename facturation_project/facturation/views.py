# facturation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import *
from django.contrib import messages
from .models import Facture
from .forms import FactureForm


#the login views
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import SignUpForm

# ...

@user_passes_test(lambda user: not user.is_authenticated, login_url='facturation:homepage')
def register_user(request):
    msg = None
    form = SignUpForm(request.POST)
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("facturation:homepage")

        else:
            msg = 'Form is not valid'

    return render(request, "templates/facturation/register.html", {"form": form, "msg": msg})

def login_view(request):
    if request.user.is_authenticated:
        return redirect("facturation:homepage")
        
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            else:
                return redirect("facturation:homepage")
        else:
            form = AuthenticationForm()
            return render(request, 'facturation/login.html', {'form': form})
     
    else:
        form = AuthenticationForm()
        return render(request, 'facturation/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('facturation:login')






#the homepage view
@login_required(login_url='facturation:login')
def homepage(request):
    if request.method == 'POST':
        facture_form = FactureForm(request.POST)
        fournisseur_form = FournisseurForm(request.POST)
        service_form = ServiceForm(request.POST)

        if facture_form.is_valid():
            facture_form.save()
            return redirect('facturation:homepage')
        if fournisseur_form.is_valid():
            fournisseur_form.save()
            return redirect('facturation:homepage')
        if service_form.is_valid():
            service_form.save()
            return redirect('facturation:homepage')

    else:
        facture_form = FactureForm()
        fournisseur_form = FournisseurForm()
        service_form = ServiceForm()
    factures = Facture.objects.all()  # This is for the homepage view
    form = SearchForm(request.GET)  # This is for the homepage view

    return render(request, 'facturation/homepage.html', { 'factures': factures,
        'facture_form': facture_form,
        'fournisseur_form': fournisseur_form,
        'service_form': service_form,
        'form':form  # This ensures the filter form is also present on the page
    })



#the sidebar view 

@login_required(login_url='facturation:login')
def profile(request):
    if request.method == 'POST':
        facture_form = FactureForm(request.POST)
        fournisseur_form = FournisseurForm(request.POST)
        service_form = ServiceForm(request.POST)

        if facture_form.is_valid():
            facture_form.save()
            return redirect('facturation:homepage')
        if fournisseur_form.is_valid():
            fournisseur_form.save()
            return redirect('facturation:homepage')
        if service_form.is_valid():
            service_form.save()
            return redirect('facturation:homepage')

    else:
        facture_form = FactureForm()
        fournisseur_form = FournisseurForm()
        service_form = ServiceForm()
    user = request.user
    return render(request, 'facturation/profile.html', {'user': user,'facture_form': facture_form,
        'fournisseur_form': fournisseur_form,
        'service_form': service_form,
        })


@login_required(login_url='facturation:login')
def services(request):
    if request.method == 'POST':
        facture_form = FactureForm(request.POST)
        fournisseur_form = FournisseurForm(request.POST)
        service_form = ServiceForm(request.POST)

        if facture_form.is_valid():
            facture_form.save()
            return redirect('facturation:homepage')
        if fournisseur_form.is_valid():
            fournisseur_form.save()
            return redirect('facturation:homepage')
        if service_form.is_valid():
            service_form.save()
            return redirect('facturation:homepage')

    else:
        facture_form = FactureForm()
        fournisseur_form = FournisseurForm()
        service_form = ServiceForm()
    services = Service.objects.all()
    return render(request, 'facturation/service.html', {'services': services,'facture_form': facture_form,
        'fournisseur_form': fournisseur_form,
        'service_form': service_form,
    })


@login_required(login_url='facturation:login')
def fournisseurs(request): 
    if request.method == 'POST':
        facture_form = FactureForm(request.POST)
        fournisseur_form = FournisseurForm(request.POST)
        service_form = ServiceForm(request.POST)

        if facture_form.is_valid():
            facture_form.save()
            return redirect('facturation:homepage')
        if fournisseur_form.is_valid():
            fournisseur_form.save()
            return redirect('facturation:homepage')
        if service_form.is_valid():
            service_form.save()
            return redirect('facturation:homepage')

    else:
        facture_form = FactureForm()
        fournisseur_form = FournisseurForm()
        service_form = ServiceForm()
    Fournisseurs=Fournisseur.objects.all()
    return render(request, 'facturation/fournisseurs.html',{'Fournisseurs':Fournisseurs,'facture_form': facture_form,
        'fournisseur_form': fournisseur_form,
        'service_form': service_form,
        })



#the header view 
@login_required(login_url='facturation:login')
def add_facture(request):
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturation:homepage')
    else:
        form = FactureForm()
    return render(request, 'facturation/add_facture.html', {'form': form})

@login_required(login_url='facturation:login')
def add_fournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            fournisseur_name = form.cleaned_data['name']
            if Fournisseur.objects.filter(name=fournisseur_name).exists():
                # Supplier with this name already exists, show an error message
                messages.error(request, f"Fournisseur '{fournisseur_name}' already exists.")
            else:
                form.save()
                return redirect('facturation:homepage')
    else:
        form = FournisseurForm()
    return render(request, 'facturation/add_fournisseur.html', {'form': form})

@login_required(login_url='facturation:login')
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            service_name = form.cleaned_data['name']
            if Service.objects.filter(name=service_name).exists():
                # Supplier with this name already exists, show an error message
                messages.error(request, f"Service '{service_name}' already exists.")
            else:
                form.save()
                return redirect('facturation:homepage')
    else:
        form = ServiceForm()
    return render(request, 'facturation/add_service.html', {'form': form})

@login_required(login_url='facturation:login')
def search(request):
     
        form = SearchForm(request.GET)
        factures = Facture.objects.all()

        if form.is_valid():
            fournisseur = form.cleaned_data['fournisseur']
            service = form.cleaned_data['service']
            date = form.cleaned_data['date']

            if fournisseur:
                factures = factures.filter(fournisseur=fournisseur)
            if service:
                factures = factures.filter(service=service)
            if date:
                factures = factures.filter(date_facture=date)
    
        return render(request,'facturation/homepage.html',{'factures':factures,})

# The crud views

#crud factures
@login_required(login_url='facturation:login')
def view_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    return render(request, 'facturation/view_facture.html', {'facture': facture})


@login_required(login_url='facturation:login')
def update_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, instance=facture)
        if form.is_valid():
            form.save()
            return redirect('facturation:view_facture', pk=pk)
    else:
        form = FactureForm(instance=facture)
    return render(request, 'facturation/update_facture.html', {'form': form, 'facture': facture})

@login_required(login_url='facturation:login')
def delete_facture(request, pk):
    facture = get_object_or_404(Facture, pk=pk)
    if request.method == 'POST':
        facture.delete()
        return redirect('facturation:homepage')
    return render(request, 'facturation/delete_facture.html', {'facture': facture})



#crud services
@login_required(login_url='facturation:login')
def view_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'facturation/view_service.html', {'service': service})
@login_required(login_url='facturation:login')
def update_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('facturation:view_service', pk=pk)
    else:
        form = ServiceForm(instance=service)
    return render(request, 'facturation/update_service.html', {'form': form, 'service': service})
@login_required(login_url='facturation:login')
def delete_service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('facturation:services')
    return render(request, 'facturation/delete_service.html', {'service': service})





#crud suppliers
@login_required(login_url='facturation:login')
def view_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    return render(request, 'facturation/view_fournisseur.html', {'fournisseur': fournisseur})
@login_required(login_url='facturation:login')
def update_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        form = FournisseurForm(request.POST, instance=fournisseur)
        if form.is_valid():
            form.save()
            return redirect('facturation:view_fournisseur', pk=pk)
    else:
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'facturation/update_fournisseur.html', {'form': form, 'fournisseur': fournisseur})
@login_required(login_url='facturation:login')
def delete_fournisseur(request, pk):
    fournisseur = get_object_or_404(Fournisseur, pk=pk)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('facturation:fournisseurs')
    return render(request, 'facturation/delete_fournisseur.html', {'fournisseur': fournisseur})



