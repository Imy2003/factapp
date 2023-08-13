# facturation/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name= 'facturation'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.homepage, name='homepage'),
    path('homepage/', views.homepage, name='homepage'),
    path('add_fournisseur/', views.add_fournisseur, name='add_fournisseur'),
    path('add_service/', views.add_service, name='add_service'),
    path('add_facture/', views.add_facture, name='add_facture'),
    path('search_factures/', views.search_factures, name='search_factures'),
    path('facture/<int:pk>/', views.view_facture, name='view_facture'),
    path('facture/<int:pk>/update/', views.update_facture, name='update_facture'),
    path('facture/<int:pk>/delete/', views.delete_facture, name='delete_facture'),

]
