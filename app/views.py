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
import random


@login_required(login_url="login")
def home_page(request):
    context = {}
    return render(request, "home.html", context)


def registration_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
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


# def dating_profile_register(request):
#     form = DatingProfileForm()
#     user = request.user.profile
#     if request.method == "POST":
#         form = DatingProfileForm(request.POST)

#     if request.method == "POST":
#         form = DatingProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form = form.save(commit=False)
#             gender = request.POST.get("gender")
#             age = request.POST.get("age")
#             interested_in = request.POST.get("interested_in")
#             smoker = request.POST.get("smoker")
#             profile_pic = request.FILES.get("profile_pic")
#             createdatingProfile(user, profile_pic, gender, age, interested_in, smoker)
#             user.has_dating_profile = True
#             user.save()
#             return redirect("personality")

#         user.has_dating_profile = True
#         user.save()
#         return redirect("personality")
#     else:
#         form = DatingProfileForm()

#     context = {"form": form, "user": user}
#     return render(request, "dating_form.html", context)


def dating_profile_register(request):
    user_profile = request.user.profile
    dating_profile, created = DatingProfile.objects.get_or_create(
        user_profile=user_profile
    )
    if request.method == "POST":
        form = DatingProfileForm(request.POST, instance=dating_profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created = True
            new_form.save()

            user_profile.has_dating_profile = True
            user_profile.save()
            return redirect("profile")
    else:
        form = DatingProfileForm(instance=dating_profile)
    context = {"form": form}
    return render(request, "dating_form.html", context)


def personality_register(request):
    user_profile = request.user.profile
    personality_profile, created = PersonalityProfile.objects.get_or_create(
        user_profile=user_profile
    )
    if request.method == "POST":
        form = PersonalityForm(request.POST, instance=personality_profile)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.created = True
            new_form.save()
            return redirect("profile")
    else:
        form = PersonalityForm()
    context = {"form": form}
    return render(request, "personality_form.html", context)


def profileView(request):
    user = request.user
    user_profile = request.user.profile
    dating_profile, created = DatingProfile.objects.get_or_create(
        user_profile=user_profile
    )
    personality_profile, created = PersonalityProfile.objects.get_or_create(
        user_profile=user_profile
    )
    context = {
        "user": user,
        "user_profile": user_profile,
        "dating_profile": dating_profile,
        "personality_profile": personality_profile,
    }
    return render(request, "userProfile.html", context)


def matchmakingView(request):
    user = User.objects.filter(id=request.user.id)

    user_dating_profile = DatingProfile.objects.get(user_profile=user).interested_in
    user_personality_profile = PersonalityProfile.objects.get(user_profile=user)

    # choices
    potentialPartners_Sexual_Preference = DatingProfile.objects.filter(
        interested_in=user_dating_profile
    )
    potentialPartners_interests = PersonalityProfile.objects.filter(
        interests=user_personality_profile.interests
    )
    potentialPartners_music = PersonalityProfile.objects.filter(
        music_pick=user_personality_profile.music_pick
    )
    potentialPartners_fun_pick = PersonalityProfile.objects.filter(
        what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick
    )
    potentialPartner_drinker = PersonalityProfile.objects.filter(
        do_you_like_drinking=user_personality_profile.do_you_like_drinking
    )
    potentialPartner_outdoor_or_indoor = PersonalityProfile.objects.filter(
        outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick
    )
    potentialPartner_movie_pick = PersonalityProfile.objects.filter(
        movie_pick=user_personality_profile.movie_pick
    )

    choices = {
        "1": [
            potentialPartners_Sexual_Preference,
            potentialPartners_interests,
            potentialPartners_music,
            potentialPartners_fun_pick,
        ],
        "2": [
            potentialPartners_Sexual_Preference,
            potentialPartner_drinker,
            potentialPartner_outdoor_or_indoor,
            potentialPartner_movie_pick,
        ],
        "3": [
            potentialPartners_Sexual_Preference,
            potentialPartner_drinker,
            potentialPartners_music,
            potentialPartner_movie_pick,
        ],
        "4": [
            potentialPartners_Sexual_Preference,
            potentialPartners_interests,
            potentialPartner_outdoor_or_indoor,
            potentialPartners_fun_pick,
        ],
    }

    random_potential_partners = random.choice(list(choices.items()))
    context = {"random_potental_partners": random_potential_partners}

    return render(request, "matchmaking.html", context)
