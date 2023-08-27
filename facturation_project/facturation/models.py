
# facturation/models.py
from django.db import models
from datetime import timedelta
from django import forms
from django.contrib.auth.models import User

#class LoginForm(forms.Form):
    #username = forms.CharField(max_length=150)
    #password = forms.CharField(widget=forms.PasswordInput)



class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Fournisseur(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Facture(models.Model):
    numero = models.CharField(max_length=20)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_facture = models.DateField()
    date_depot = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    
    status = models.CharField(choices=(('draft', 'Draft'), ('validated', 'Validated'), ('paid', 'Paid')), default='draft', max_length=20)
    echeance = models.DateField(blank=True, null=True)  

    def __str__(self):
        return f"{self.numero} - {self.fournisseur} - {self.montant}"

    def save(self, *args, **kwargs):
        if not self.echeance:  # Calculate échéance date only if it's not set
            self.echeance = self.date_facture + timedelta(days=90)
        super(Facture, self).save(*args, **kwargs)