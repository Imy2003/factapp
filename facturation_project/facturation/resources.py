from import_export import resources, fields
from .models import Facture
class FactureResource(resources.ModelResource):
    fournisseur = fields.Field(column_name='Fournisseur', attribute='fournisseur__name')
    service = fields.Field(column_name='Service', attribute='service__name')

    class Meta:
        model = Facture
        fields = ('numero', 'fournisseur', 'date_facture', 'date_depot', 'echeance', 'service', 'montant', 'status')
