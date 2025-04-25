from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .forms import *
# Create your views here.

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = "dashboard/pages/home.html"

class LoginPage(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

class UserPage(TemplateView):
    template_name = "dashboard/pages/add_superuser.html"

class StudentPage(TemplateView):
    template_name = "dashboard/pages/add_student.html"
