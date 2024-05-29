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
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("first_name")
            Profile.objects.create(
                user=user, first_name=first_name, last_name=last_name
            )
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


def dating_profile_register(request):
    user_profile = request.user.profile
    dating_profile, created = DatingProfile.objects.get_or_create(
        user_profile=user_profile
    )
    if request.method == "POST":
        form = DatingProfileForm(request.POST, request.FILES, instance=dating_profile)
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
    user_get = request.user.profile
    dating_profile = DatingProfile.objects.get(user_profile=user_get)

    personality_profile, created = PersonalityProfile.objects.get_or_create(
        user_profile=dating_profile
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
        user_profile=dating_profile
    )
    dating_profile = DatingProfile.objects.get(user_profile=user_profile)
    context = {
        "user": user,
        "user_profile": user_profile,
        "dating_profile": dating_profile,
        "personality_profile": personality_profile,
    }
    return render(request, "userProfile.html", context)


def matchmakingView(request):
    # user = User.objects.filter(id=request.user.id)
    user = request.user.profile

    user_dating_profile = DatingProfile.objects.get(user_profile=user)
    user_personality_profile = PersonalityProfile.objects.get(
        user_profile=user_dating_profile
    )
    # user_dating_profile = DatingProfile.objects.get(user_profile=user).interested_in
    # user_personality_profile = PersonalityProfile.objects.get(user_profile=user)

    # choices
    # potentialPartners_Sexual_Preference = DatingProfile.objects.filter(
    #     interested_in=user_dating_profile
    # )
    # potentialPartners_interests = PersonalityProfile.objects.filter(
    #     interests=user_personality_profile.interests
    # )
    # potentialPartners_music = PersonalityProfile.objects.filter(
    #     music_pick=user_personality_profile.music_pick
    # )
    # potentialPartners_fun_pick = PersonalityProfile.objects.filter(
    #     what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick
    # )
    # potentialPartner_drinker = PersonalityProfile.objects.filter(
    #     do_you_like_drinking=user_personality_profile.do_you_like_drinking
    # )
    # potentialPartner_outdoor_or_indoor = PersonalityProfile.objects.filter(
    #     outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick
    # )
    # potentialPartner_movie_pick = PersonalityProfile.objects.filter(
    #     movie_pick=user_personality_profile.movie_pick
    # )
    choice2 = PersonalityProfile.objects.filter(
        # user_profile__interested_in=user_dating_profile,
        do_you_like_drinking=user_personality_profile.do_you_like_drinking,
        outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick,
        movie_pick=user_personality_profile.movie_pick,
    )
    choice3 = PersonalityProfile.objects.filter(
        # user_profile__interested_in=user_dating_profile,
        do_you_like_drinking=user_personality_profile.do_you_like_drinking,
        music_pick=user_personality_profile.music_pick,
        movie_pick=user_personality_profile.movie_pick,
    )
    choice4 = PersonalityProfile.objects.filter(
        # user_profile__interested_in=user_dating_profile,
        interests=user_personality_profile.interests,
        outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick,
        what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick,
    )
    choice1 = PersonalityProfile.objects.filter(
        # user_profile__interested_in=user_dating_profile,
        interests=user_personality_profile.interests,
        music_pick=user_personality_profile.music_pick,
        what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick,
    )
    choices = {
        "1": [choice1],
        "2": [choice2],
        "3": [choice3],
        "4": [choice4],
    }

    random_potential_partners = key, val = random.choice(list(choices.items()))
    context = {
        "random_potential_partners": random_potential_partners,
        "key": key,
        "val": val,
    }

    return render(request, "matchmaking.html", context)
