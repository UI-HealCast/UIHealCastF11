from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from landing.models import Landing

# Create your models here.
class Obat(models.Model):
    nama_obat = models.CharField(max_length=255, null=True)
    harga = models.IntegerField(null=True)
    status_obat = models.BooleanField(null=True, blank=True)
    description = models.TextField(null=True)