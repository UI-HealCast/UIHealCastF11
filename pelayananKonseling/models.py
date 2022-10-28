from email.policy import default
from django.db import models
from landing.models import Landing

# Create your models here.
class PelayananKonseling(models.Model):
    user = models.ForeignKey(Landing, on_delete=models.CASCADE, null=True, blank=True, related_name='user_pelayananKonseling')

    username = models.CharField(max_length=30, default='-')

    nama = models.CharField(max_length=30, default='-')
    status_user = models.CharField(max_length=20, default='-') #dropdown (Mahasiswa UI, Pegawai UI, Others)
    noHP = models.CharField(max_length=12)
    email = models.EmailField(max_length=50, default='-')
    bentuk_konseling = models.CharField(max_length=30, default='-') #dropdown (Offline, Online via chat, Online via video call)
    keluhan_konseling = models.TextField(default='-')

    def __str__(self):
        return self.nama

class PreferensiHari(models.Model):
    user = models.ForeignKey(PelayananKonseling, on_delete=models.CASCADE, null=True, blank=True, related_name='user_preferensiHari')
    senin = models.BooleanField(default=False)
    selasa = models.BooleanField(default=False)
    rabu = models.BooleanField(default=False)
    kamis = models.BooleanField(default=False)
    jumat = models.BooleanField(default=False)
    sabtu = models.BooleanField(default=False)
    minggu = models.BooleanField(default=False)

class PreferensiWaktu(models.Model):
    user = models.ForeignKey(PelayananKonseling, on_delete=models.CASCADE, null=True, blank=True, related_name='user_preferensiWaktu')
    pagi = models.BooleanField(default=False)
    siang = models.BooleanField(default=False)
    sore = models.BooleanField(default=False)
    malam = models.BooleanField(default=False)



    
