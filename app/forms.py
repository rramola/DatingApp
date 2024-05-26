from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)
    fname = forms.CharField(max_length=255)
    lname = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "fname",
            "lname"
        ]