 from popup_field.views import PopupCRUDViewSet
 from.forms import *
 from .models import *
  
 
 class FournisseurPopupCRUDViewSet(PopupCRUDViewSet):
     model = Fournisseur
     form_class = FournisseurForm
     template_name_create = 'popup/delete.html'
     template_name_update = 'popup/update.html'

 class ServiceCRUDViewSet(PopupCRUDViewSet):
     model = Service
     form_class = ServiceForm
     template_name_create = 'popup/delete.html'
     template_name_update = 'popup/update.html'