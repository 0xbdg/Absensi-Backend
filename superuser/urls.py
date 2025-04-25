from django.urls import path 
from .views import *

urlpatterns = [
    path("dashboard/", DashboardPage.as_view(), name="home"),
    path("login/", LoginPage.as_view(), name="login"),
    path("add_superuser/", UserPage.as_view(), name="add_superuser"),
    path("add_student/", StudentPage.as_view(), name="add_student"),
]
