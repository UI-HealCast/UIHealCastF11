from datetime import datetime
from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
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

    hasilPeriksa = models.CharField(max_length=150, default='-')