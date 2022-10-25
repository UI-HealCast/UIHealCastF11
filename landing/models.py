from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Landing(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    is_patient = models.BooleanField(null=True, blank=True)
    is_doctor = models.BooleanField(null=True, blank=True, default=False)
    is_apotek = models.BooleanField(null=True, blank=True, default=False)
    is_admin = models.BooleanField(null=True, blank=True, default=False)