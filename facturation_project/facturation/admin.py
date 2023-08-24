from django.contrib import admin
from .models import Facture, Fournisseur,  Service
from .resources import FactureResource  # Import the resource

class FactureAdmin(admin.ModelAdmin):
    resource_class = FactureResource

admin.site.register(Facture, FactureAdmin)

