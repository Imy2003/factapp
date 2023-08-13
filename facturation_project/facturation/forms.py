# facturation/forms.py
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Facture, Fournisseur, Service


#class FactureForm(forms.ModelForm):
    #class Meta:
        #model = Facture
        #fields = '__all__'


#class LoginForm(forms.Form):
    #username = forms.CharField(
     #   widget=forms.TextInput(
      #      attrs={
       #         "placeholder": "Username",
        #        "class": "form-control"
         #   }
        #))
    #password = forms.CharField(
     #   widget=forms.PasswordInput(
      #      attrs={
       #         "placeholder": "Password",
        #        "class": "form-control"
         #   }
        #))
    

class SignUpForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

class LoginForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','password']


class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['name', 'email', 'phone']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name']

class FactureForm(forms.ModelForm):
    class Meta:
        model = Facture
        fields = ['numero', 'fournisseur', 'date_facture', 'date_depot', 'service', 'status','montant']


class SearchForm(forms.Form):
    fournisseur = forms.ModelChoiceField(queryset=Fournisseur.objects.all(), empty_label="Select Fournisseur", required=False)
    service = forms.ModelChoiceField(queryset=Service.objects.all(), empty_label="Select Service", required=False)
    date = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))