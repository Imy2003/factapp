# facturation:login/urls.py
from django.urls import path
from . import views

 
app_name= 'facturation'
urlpatterns = [
    #login paths
    path('register/', views.register_user, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    #homepage paths
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage'),
    #sidebar paths

    path('factures',views.homepage,name='factures'),
    path('fournisseurs/',views.fournisseurs,name='fournisseurs'),
    path('services/', views.services, name='services'),
    #CRUD for Factures
    path('add_facture/', views.add_facture, name='add_facture'),
    path('facture/<int:pk>/', views.view_facture, name='view_facture'),
    path('facture/<int:pk>/update/', views.update_facture, name='update_facture'),
    path('facture/<int:pk>/delete/', views.delete_facture, name='delete_facture'),
    # CRUD for Fournisseurs
    path('fournisseur/add/', views.add_fournisseur, name='add_fournisseur'),
    path('fournisseur/<int:pk>/', views.view_fournisseur, name='view_fournisseur'),
    path('fournisseur/<int:pk>/update/', views.update_fournisseur, name='update_fournisseur'),
    path('fournisseur/<int:pk>/delete/', views.delete_fournisseur, name='delete_fournisseur'),
    # CRUD for Services
    path('service/add/', views.add_service, name='add_service'),
    path('service/<int:pk>/', views.view_service, name='view_service'),
    path('service/<int:pk>/update/', views.update_service, name='update_service'),
    path('service/<int:pk>/delete/', views.delete_service, name='delete_service'),
    #exporting_importing
    path('export/', views.export_data, name="export_data"),

]
