from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.forms import *
from absensi.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={"class":""}))
    password = forms.CharField(required=True, widget=PasswordInput(attrs={"class":""}))

class SuperuserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(SuperuserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_staff = True
        user.is_superuser = True
        if commit:
            user.save()
        return user
    
class SuperuserUpdateForm(UserChangeForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label='New Password')
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label='Confirm Password')
    class Meta:
        model = User
        fields = ['username', 'email',"password"]

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords do not match.")