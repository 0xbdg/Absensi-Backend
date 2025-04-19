from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("absensi.urls")),
    path("superuser/", include("superuser.urls")),
    path('admin/', admin.site.urls),
]
