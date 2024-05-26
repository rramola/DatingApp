from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group



# Create your views here.
from .forms import *
from .models import *


@login_required(login_url="login")
def home_page(request):
    context = {}
    return render(request, "home.html", context)

def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            fname = form.cleaned_data.get("fname")
            lname = form.cleaned_data.get("lname")
            UserProfile.objects.create(user=user, fname=fname, lname=lname)
            messages.success(request, "Account was created for" + " " + username)
            return redirect("home")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "register.html", context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Username or password is incorrect.")
            return render(request, "login.html")
    context = {}
    return render(request, "login.html", context)

@login_required(login_url="login")
def logout_user(request):
    logout(request)
    return redirect("login")