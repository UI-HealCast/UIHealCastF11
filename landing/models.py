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
    doctorReady = models.BooleanField(null=True, default=False)   
    username = models.CharField(max_length=30, default='-') 


    def __str__(self):
        return self.username