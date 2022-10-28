from django import forms
from django.forms import ModelForm
from .models import *

class PelayananKonselingForm(ModelForm):
    class Meta:
        model = PelayananKonseling
        fields = ['nama', 'status_user', 'noHP', 'email', 'bentuk_konseling', 'keluhan_konseling']

class PreferensiHariForm(ModelForm):
    class Meta:
        model = PreferensiHari
        fields = ['senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu']

class PreferensiWaktuForm(ModelForm):
    class Meta:
        model = PreferensiWaktu
        fields = ['pagi', 'siang', 'sore', 'malam']