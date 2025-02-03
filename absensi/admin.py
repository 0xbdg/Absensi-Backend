from django.contrib import admin
from .models import Siswa

# Register your models here.

class CustomSiswa(admin.ModelAdmin):
    model = Siswa
    list_display = ["uid","nama", "kelas", "jurusan"]

    list_filter = ["kelas", "jurusan"]

admin.site.register(Siswa, CustomSiswa)