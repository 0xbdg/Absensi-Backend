from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":""}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":""}))