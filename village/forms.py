from django import forms
from . import models
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    Логин = forms.CharField()
    Пароль = forms.CharField(widget=forms.PasswordInput)
