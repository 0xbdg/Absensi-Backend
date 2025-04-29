from django.urls import path 
from .views import *

urlpatterns = [
    path("dashboard/", DashboardPage.as_view(), name="home"),
    path("login/", LoginPage.as_view(), name="login"),
    path("account/", UserPage.as_view(), name="superuser"),
    path("student/", StudentPage.as_view(), name="student"),
    path("account/add/", CreateSuperuserPage.as_view(), name="add_superuser"),
    path("account/update/<int:pk>/", UpdateSuperuserPage.as_view(), name="update_superuser"),
    path("account/delete/<int:pk>", DeleteSuperuser.as_view(), name="delete_superuser"),
    path("student/add/", CreateStudentPage.as_view(), name="add_student"),
    path("student/update/<int:pk>/", UpdateStudentPage.as_view(), name="update_student"),
    path("student/delete/<int:pk>/", DeleteStudent.as_view(), name="delete_student")
]
