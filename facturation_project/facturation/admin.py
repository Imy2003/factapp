from django.contrib import admin
from .models import Facture, Fournisseur,  Service
admin.site.register(Facture)
admin.site.register(Fournisseur)

admin.site.register(Service)