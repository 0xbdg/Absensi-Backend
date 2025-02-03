from django.shortcuts import render
from django.http import JsonResponse
from .models import Siswa
# Create your views here.

def siswa(request, uid):
    siswa = Siswa.objects.get(uid=uid)

    data = {
        "nama":siswa.nama,
        "kelas":siswa.kelas,
        "jurusan":siswa.jurusan
    }
    return JsonResponse(data)