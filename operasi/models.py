from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Operasi(models.Model):
    dokter = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    pasien = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    jenis = models.CharField()
    tanggal = models.CharField()
    jam = models.CharField()
    durasi = models.CharField()
    keterangan = models.TextField()

