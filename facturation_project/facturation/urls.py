# facturation/urls.py
from django.urls import path
from . import views
app_name= 'facturation'
urlpatterns = [
    path('', views.login_view, name='login'),
   
    path('register/', views.register_user, name='register'),
]
