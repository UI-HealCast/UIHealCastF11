from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
import datetime

from landing.models import Landing
from pelayananDokter.models import Layan

class Bayar(models.Model):
    user = models.ForeignKey(Landing, on_delete=models.CASCADE, null=True, blank=True, related_name = "landing_user")
