# facturation/urls.py
from django.urls import path
from . import views
app_name= 'facturation'
urlpatterns = [
    path('create_facture/', views.create_facture, name='create_facture'),
    path('facture_list/', views.facture_list, name='facture_list'),
    path('', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
]
