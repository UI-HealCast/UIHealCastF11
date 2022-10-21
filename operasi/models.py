from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Operasi(models.Model):
    dokter = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="dokter")
    pasien = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="pasien")
    jenis = models.CharField(max_length = 30)
    tanggal = models.CharField(max_length = 30)
    jam = models.CharField(max_length = 30)
    durasi = models.CharField(max_length = 30)
    keterangan = models.TextField()

