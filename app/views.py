from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ValidationError

# Create your views here.
from .forms import *
from .models import *
import random


@login_required(login_url="login")
def base(request):
    user = request.user
    context = {"user": user}
    return render(request, "base.html", context)


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


@login_required(login_url="login")
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
            if new_form.age < 18:
                raise ValidationError("You must be 18 years or older")
            return redirect("profile")
    else:
        form = DatingProfileForm(instance=dating_profile)
    context = {"form": form}
    return render(request, "dating_form.html", context)


@login_required(login_url="login")
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


@login_required(login_url="login")
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


@login_required(login_url="login")
def deleteProfile(request):
    user = request.user
    user.delete()
    return redirect("login")


@login_required(login_url="login")
def partner_profile_view(request, id):
    dating_profile = DatingProfile.objects.get(id=id)
    context = {
        "dating_profile": dating_profile,
        # "partner": partner,
    }
    return render(request, "potiental_partner_profile.html", context)


@login_required(login_url="login")
def matchmakingView(request):
    # user = User.objects.filter(id=request.user.id)
    user_profile = request.user.profile
    user = request.user
    user_dating_profile = DatingProfile.objects.get(user_profile=user_profile)
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
        user_profile__interested_in=user_dating_profile.interested_in,
        do_you_like_drinking=user_personality_profile.do_you_like_drinking,
        outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick,
        movie_pick=user_personality_profile.movie_pick,
        hobby_pick=user_personality_profile.hobby_pick,
    )
    choice3 = PersonalityProfile.objects.filter(
        user_profile__interested_in=user_dating_profile.interested_in,
        do_you_like_drinking=user_personality_profile.do_you_like_drinking,
        music_pick=user_personality_profile.music_pick,
        movie_pick=user_personality_profile.movie_pick,
        sport_pick=user_personality_profile.sport_pick,
    )
    choice4 = PersonalityProfile.objects.filter(
        user_profile__interested_in=user_dating_profile.interested_in,
        interests=user_personality_profile.interests,
        outdoor_indoor_pick=user_personality_profile.outdoor_indoor_pick,
        what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick,
        hobby_pick=user_personality_profile.hobby_pick,
    )
    choice1 = PersonalityProfile.objects.filter(
        user_profile__interested_in=user_dating_profile.interested_in,
        interests=user_personality_profile.interests,
        music_pick=user_personality_profile.music_pick,
        what_do_you_do_for_fun_pick=user_personality_profile.what_do_you_do_for_fun_pick,
        sport_pick=user_personality_profile.sport_pick,
    )
    choices = {
        "1": [choice1],
        "2": [choice2],
        "3": [choice3],
        "4": [choice4],
    }

    random_potential_partners = key, val = random.choice(list(choices.items()))
    # Collect the user's personality data
    user_data_list = [
        user_personality_profile.id,
        user_personality_profile.interests,
        user_personality_profile.user_profile.interested_in,
        user_personality_profile.do_you_like_drinking,
        user_personality_profile.are_you_active,
        user_personality_profile.music_pick,
        user_personality_profile.outdoor_indoor_pick,
        user_personality_profile.what_do_you_do_for_fun_pick,
        user_personality_profile.movie_pick,
    ]

    # Initialize list to store compatible profiles
    compatible_personality_profiles_list = []
    # Iterate through all personality profiles in the database
    for profile in PersonalityProfile.objects.all():
        profile_data = {
            "id": profile.id,
            "interests": profile.interests,
            "interested_in": profile.user_profile.interested_in,
            "drinking": profile.do_you_like_drinking,
            "active": profile.are_you_active,
            "music": profile.music_pick,
            "outdoor_indoor": profile.outdoor_indoor_pick,
            "fun": profile.what_do_you_do_for_fun_pick,
            "movie": profile.movie_pick,
        }

        matches = 0
        for user_value, profile_value in zip(user_data_list, profile_data.values()):
            if user_value == profile_value:
                matches += 1
            # Check for compatibility

        if matches > 3:
            compatible_personality_profiles_list.append(profile)

        match_list = []
        for object in compatible_personality_profiles_list:
            if (
                user_dating_profile.interested_in == "Men"
                and user_dating_profile.gender == "Male"
                and object.user_profile.interested_in == "Men"
                and object.user_profile.gender == "Male"
            ):
                match_list.append(object)
            elif (
                user_dating_profile.interested_in == "Women"
                and user_dating_profile.gender == "Female"
                and object.user_profile.interested_in == "Women"
                and object.user_profile.gender == "Female"
            ):
                match_list.append(object)
            elif (
                user_dating_profile.interested_in == "Men"
                and user_dating_profile.gender == "Female"
                and object.user_profile.interested_in == "Women"
                and object.user_profile.gender == "Male"
            ):
                match_list.append(object)
            elif (
                user_dating_profile.interested_in == "Women"
                and user_dating_profile.gender == "Male"
                and object.user_profile.interested_in == "Men"
                and object.user_profile.gender == "Women"
            ):
                match_list.append(object)
            elif (
                user_dating_profile.interested_in == "Both"
                and user_dating_profile.gender == "Male"
                and object.user_profile.interested_in == "Both"
                and object.user_profile.gender == "Women"
                or user_dating_profile.interested_in == "Both"
                and user_dating_profile.gender == "Female"
                and object.user_profile.interested_in == "Both"
                and object.user_profile.gender == "Male"
            ):
                match_list.append(object)

    context = {
        "random_potential_partners": random_potential_partners,
        "key": key,
        "val": val,
        "user_profile": user_profile,
        "user": user,
        "user_profile": user_profile,
        "user_dating_profile": user_dating_profile,
        "compatible_personality_profiles": compatible_personality_profiles_list,
        "match_list": match_list,
    }

    return render(request, "matchmaking.html", context)


@login_required(login_url="login")
def messagesView(request, id):
    user = Profile.objects.get(user__id=id)
    messages = Message.objects.filter(recipient=user)
    context = {"messages": messages}
    if request.method == "POST":
        content = request.POST.get("content")
        new_message = Message.objects.create(
            sender=request.user.profile,
            recipient=user,
            content=content,
        )
        new_message.save()
    return render(request, "messages.html", context)


@login_required(login_url="login")
def send_message(request, recipient_id):
    if request.method == "POST":
        sender = request.user.profile
        recipient = Profile.objects.get(id=recipient_id)
        content = request.POST.get("content")
        message = Message.objects.create(
            sender=sender, recipient=recipient, content=content
        )
        return redirect("inbox")
    else:
        recipient = Profile.objects.get(id=recipient_id)
        return render(request, "send_message.html", {"recipient": recipient})


# THREAD ATTEMPT
# @login_required
# def send_message(request, recipient_id, parent_message_id=None):
#     if request.method == 'POST':
#         sender = request.user.profile
#         recipient = Profile.objects.get(id=recipient_id)
#         content = request.POST.get('content')
#         if parent_message_id:
#             parent_message = Message.objects.get(id=parent_message_id)
#             message = Message.objects.create(sender=sender, recipient=recipient, content=content, parent_message=parent_message)
#         else:
#             message = Message.objects.create(sender=sender, recipient=recipient, content=content)
#         return redirect('inbox')
#     else:
#         recipient = Profile.objects.get(id=recipient_id)
#         parent_message = None
#         if parent_message_id:
#             parent_message = Message.objects.get(id=parent_message_id)
#         return render(request, 'send_message.html', {'recipient': recipient, 'parent_message': parent_message})


@login_required(login_url="login")
def inbox(request):
    user = request.user.profile
    received_messages = Message.objects.filter(recipient=user)
    sent_messages = Message.objects.filter(sender=user)
    return render(
        request,
        "inbox.html",
        {"received_messages": received_messages, "sent_messages": sent_messages},
    )


@login_required(login_url="login")
def message_detail(request, message_id):
    message = Message.objects.get(id=message_id)
    if request.method == "POST":
        content = request.POST.get("content")
        reply = Message.objects.create(
            sender=request.user.profile, recipient=message.sender, content=content
        )
        return redirect("message_detail", message_id=message_id)
    return render(request, "message_detail.html", {"message": message})
