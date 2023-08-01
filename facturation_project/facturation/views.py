# facturation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

from .forms import *
from django.contrib import messages
from django.http import HttpResponse



def register_user(request):
    msg = None
    success = False
    form= SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
 

    return render(request, "templates/register.html", {"form": form, "msg": msg, "success": success})


def login_view(request):
    if request.method == "POST":
        username=request.Post.get('username')
        password=request.Post.get('password')
        user= authenticate(request, username=username, password=password)
    if user is not None:
        login(request,user)
    else:
        messages.info(request,'Username or password is incorrect  ')
        return redirect('/login/')
    context ={}
    return render(request, "templates/login.html", context)