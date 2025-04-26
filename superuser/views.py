from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import *
from .forms import *
from absensi.models import *
# Create your views here.

class DashboardPage(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages/home.html"

class LoginPage(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

class UserPage(LoginRequiredMixin,ListView):
    model = User
    template_name = "admin/pages/superuser.html"
    context_object_name = "Users"

class StudentPage(LoginRequiredMixin,TemplateView):
    template_name = "admin/pages/add_student.html"

class CreateSuperuserPage(LoginRequiredMixin,CreateView):
    model = User
    form_class=SuperuserCreationForm
    template_name = "admin/pages/superuser-crud/add_superuser.html"
    success_url = reverse_lazy("superuser")

class UpdateSuperuserPage(LoginRequiredMixin,UpdateView):
    model = User
    form_class=SuperuserUpdateForm
    template_name = "admin/pages/superuser-crud/update_account.html"
    success_url = reverse_lazy("superuser")  

class DeleteSuperuser(LoginRequiredMixin, DeleteView):
    model = User
    