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
            form.save()

            return redirect("login")
    else:
        form = RegistrationForm()
    context = {"form": form}
    return render(request, "register.html", context)


def dating_profile_register(request):
    form = DatingProfileForm()
    user = request.user
    if request.method == "POST":
        form = DatingProfileForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            gender = request.POST.get("gender")
            age = request.POST.get("age")
            interested_in = request.POST.get("interested_in")
            smoker = request.POST.get("smoker")
            profile_pic = request.FILES.get("profile_pic")

            createdatingProfile(user, profile_pic, gender, age, interested_in, smoker)

            return redirect("personality")

    context = {"form": form}
    return render(request, "dating_form.html", context)


def personality_register(request):
    if request.method == "POST":
        form = PersonalityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = PersonalityForm()
    context = {"form": form}
    return render(request, "personality_form.html", context)


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


def profileView(request):
    user = User.objects.filter(id=request.user.id)
    userProfile = DatingProfile.objects.filter(user_profile=request.user)
    print(user)
    context = {"user": user, "userProfile": userProfile}
    return render(request, "userProfile.html", context)
