# facturation:login/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
app_name= 'facturation'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', login_required(views.homepage,login_url='facturation:login'), name='homepage'),
    path('homepage/', login_required(views.homepage,login_url='facturation:login'), name='homepage'),

    path('homepage/',login_required(views.search,login_url='facturation:login'), name='homepage'),
    path('add_service/', login_required(views.add_service,login_url='facturation:login'), name='add_service'),
    path('add_facture/', login_required(views.add_facture,login_url='facturation:login'), name='add_facture'),
    path('factures',login_required(views.homepage,login_url='facturation:login'),name='factures'),
    path('facture/<int:pk>/', login_required(views.view_facture,login_url='facturation:login'), name='view_facture'),
    path('facture/<int:pk>/update/', login_required(views.update_facture,login_url='facturation:login'), name='update_facture'),
    path('facture/<int:pk>/delete/', login_required(views.delete_facture,login_url='facturation:login'), name='delete_facture'),
    path('services/',login_required(views.services,login_url='facturation:login'), name='service'),
    path('fournisseurs/',login_required(views.fournisseurs,login_url='facturation:login'),name='fournisseurs'),
    

]
