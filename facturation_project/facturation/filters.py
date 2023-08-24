import django_filters
from django_filters import DateFilter
from .models import *


class FactureFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(
        field_name='date_facture',
        lookup_expr='gte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=('De:')
    )
    
    end_date = django_filters.DateFilter(
        field_name='date_facture',
        lookup_expr='lte',
        widget=forms.DateInput(attrs={'type': 'date'}),
        label=('à:')
    )

    class Meta:
        model= Facture
        feilds='__all__'
        exclude =['numero','montant','date_depot','date_facture','echeance']

class FournisseurFilter(django_filters.FilterSet):
    class Meta:
        model=Fournisseur
        feilds='__all__'
        exclude=['email','phone']
