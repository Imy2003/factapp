# facturation/forms.py
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Facture, Fournisseur, Service


    

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        
        fields = ['username', 'email','password1','password2']




class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['name', 'email', 'phone']
    def clean_name(self):
        name = self.cleaned_data['name']
        if Fournisseur.objects.filter(name=name).exists():
            raise forms.ValidationError("This supplier already exists.")
        return name

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name']
    def clean_name(self):
        name = self.cleaned_data['name']
        if Service.objects.filter(name=name).exists():
            raise forms.ValidationError("This service already exists.")
        return name

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'fournisseur', 'date_facture', 'date_depot', 'service', 'status','montant']

class SearchView(forms.Form):
    q = forms.CharField(label="Search", max_length=200)
class SearchForm(forms.Form):
    fournisseur = forms.ModelChoiceField(queryset=Fournisseur.objects.all(), empty_label="Select Fournisseur", required=False)
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label="Select Service", required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))