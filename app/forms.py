from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from django.contrib.auth import get_user_model


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
        )


class DatingProfileForm(forms.ModelForm):
    class Meta:
        model = DatingProfile
        fields = (
            "profile_pic",
            "gender",
            "age",
            "interested_in",
            "smoker",
            "drinker",
            "occupation",
            "bio",
            "favorite_place_ever_been",
        )


class PersonalityForm(forms.ModelForm):
    class Meta:
        model = PersonalityProfile
        fields = (
            "interests",
            "do_you_like_drinking",
            "are_you_active",
            "music_pick",
            "outdoor_indoor_pick",
            "what_do_you_do_for_fun_pick",
            "movie_pick",
            "hobby_pick",
            "sport_pick",
        )
