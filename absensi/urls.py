from django.urls import path
from .views import *

urlpatterns = [
    path("data/siswa/<str:uid>", siswa)
]
