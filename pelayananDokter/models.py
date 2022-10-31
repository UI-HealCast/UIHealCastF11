from datetime import datetime
from django.db import models
from landing.models import Landing
# Create your models here.

class Layan(models.Model):
    user = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "user_pasien")

    dokter = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "dokter")

    keluhan = models.CharField(max_length=300) 
    
    tanggal_janji = models.DateTimeField(default = datetime.now)
    
    noHP = models.CharField(max_length=12)

    status = models.BooleanField(null=True, blank=True)

    username = models.CharField(max_length=30, default='-')
    usernameDokter = models.CharField(max_length=30, default='-')

    hasilPeriksa = models.CharField(max_length=150, default='-')
    
    statusObat = models.BooleanField(null=True, blank=True, default=False)
    statusBayar = models.BooleanField(null=True, blank=True, default=False)
