from django.db import models

# Create your models here.

class Siswa(models.Model):
    KELAS = (
        ("X", "X"),
        ("XI", "XI"),
        ("XII", "XII")
    )

    JURUSAN = (
        ("Perhotelan", "Perhotelan"),
        ("PPLG", "PPLG"),
        ("DKV", "DKV"),
        ("Akuntansi", "Akuntansi"),
        ("Kuliner", "Kuliner")
    )

    uid = models.CharField(max_length=255, null=False, blank=False)
    nama = models.CharField(max_length=255, null=False, blank=False)
    kelas = models.CharField(max_length=255, choices=KELAS)
    jurusan = models.CharField(max_length=255, choices=JURUSAN)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name = "Siswa"
        verbose_name_plural = "Siswa"

class Guru(models.Model):
    pass