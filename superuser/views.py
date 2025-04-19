from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class DashboardPage(TemplateView):
    template_name = "dashboard/pages/home.html"
