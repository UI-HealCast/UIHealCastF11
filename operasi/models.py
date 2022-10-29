from django.db import models
from landing.models import Landing
# Create your models here.

class Operasi(models.Model):
    dokter = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "dokter_operasi")
    usernameDokter = models.CharField(max_length=30, default='-')
    pasien = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "pasien_operasi")
    usernamePasien = models.CharField(max_length=30, default='-')
    tanggal = models.DateField()
    jam = models.TimeField()
    keterangan = models.CharField(max_length=1000)

