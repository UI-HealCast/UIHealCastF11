from email.policy import default
from random import choices
from django.db import models
from landing.models import Landing

# Create your models here.

STATUS_USER = [
    ('Mahasiswa UI', 'Mahasiswa UI'),
    ('Pegawai UI', 'Pegawai UI'),
    ('Others', 'Others'),
]

BENTUK_KONSELING = [
    ('Offline', 'Offline'),
    ('Online via chat', 'Online via chat'),
    ('Online via video call', 'Online via video call'),
]

class PelayananKonseling(models.Model):
    user = models.ForeignKey(Landing, on_delete=models.CASCADE, null=True, blank=True, related_name='user_pelayananKonseling')

    username = models.CharField(max_length=30, default='')

    nama = models.CharField(max_length=30, default='')
    status_user = models.CharField(max_length=20, default='', choices=STATUS_USER) #dropdown (Mahasiswa UI, Pegawai UI, Others)
    noHP = models.IntegerField()
    email = models.EmailField(max_length=50, default='')
    bentuk_konseling = models.CharField(max_length=30, default='', choices=BENTUK_KONSELING) #dropdown (Offline, Online via chat, Online via video call)
    keluhan_konseling = models.TextField(default='')
    status_konseling = models.BooleanField(null=True, blank=True, default=False)

    senin = models.BooleanField(default=False)
    selasa = models.BooleanField(default=False)
    rabu = models.BooleanField(default=False)
    kamis = models.BooleanField(default=False)
    jumat = models.BooleanField(default=False)
    sabtu = models.BooleanField(default=False)
    minggu = models.BooleanField(default=False)

    pagi = models.BooleanField(default=False)
    siang = models.BooleanField(default=False)
    sore = models.BooleanField(default=False)
    malam = models.BooleanField(default=False)


    def __str__(self):
        return self.nama


    


    
