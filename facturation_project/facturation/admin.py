from django.contrib import admin
from .models import Facture, Fournisseur, Client, Service
admin.site.register(Facture)
admin.site.register(Fournisseur)
admin.site.register(Client)
admin.site.register(Service)