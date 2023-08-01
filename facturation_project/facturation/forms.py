# facturation/forms.py
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



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