from django.db import models
from django.contrib.auth.models import User
from landing.models import Landing
# Create your models here.

class Layan(models.Model):
    user = models.ForeignKey(
        Landing, on_delete=models.CASCADE, null=True, blank=True)

    dokter = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    keluhan = models.CharField(max_length=255)

    nama = models.CharField(max_length=60)

    tanggal_janji = models.DateTimeField()
    
    noHP = models.CharField(max_length=12)

    status = models.BooleanField(null=True, blank=True)