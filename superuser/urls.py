from django.urls import path 
from .views import *

urlpatterns = [
    path("admin/dashboard", DashboardPage.as_view(), name="")
]
