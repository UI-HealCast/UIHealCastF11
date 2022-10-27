from django.db import models
from landing.models import Landing
# Create your models here.
class Operasi(models.Model):
    dokter = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "dokter_operasi")
    pasien = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "pasien_operasi")
    tanggal = models.CharField(max_length = 30)
    jam = models.CharField(max_length = 30)
    keterangan = models.TextField()

