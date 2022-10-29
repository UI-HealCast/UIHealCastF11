from django import forms
from django.forms import ModelForm
from .models import *
from django.utils.translation import gettext_lazy as _

STATUS_USER = [
    ('Mahasiswa UI', 'Mahasiswa UI'),
    ('Pegawai UI', 'Pegawai UI'),
    ('Others', 'Others'),
]

BENTUK_KONSELING = [
    ('Offline', 'Offline'),
    ('Online via chat', 'Online via chat'),
    ('Online via video call', 'Online via video call'),
]

class PelayananKonselingForm(ModelForm):
    class Meta:
        model = PelayananKonseling
        fields = ['nama', 'status_user', 'noHP', 'email', 'bentuk_konseling', 'keluhan_konseling', 'senin', 'selasa', 'rabu', 'kamis', 'jumat', 'sabtu', 'minggu', 'pagi', 'siang', 'sore', 'malam']

       

        labels = {
            'nama': _('Nama'),
            'noHP': _('Masukkan nomor yang dapat dihubungi'),
            'email': _('Masukkan email yang dapat dihubungi'),
            'keluhan_konseling': _('Isi keluhan'),
            'senin': _('Senin'),
            'selasa': _('Selasa'),
            'rabu': _('Rabu'),
            'kamis': _('Kamis'),
            'jumat': _('Jumat'),
            'sabtu': _('Sabtu'),
            'minggu': _('Minggu'),
            'pagi': _('Pagi'),
            'siang': _('Siang'),
            'sore': _('Sore'),
            'malam': _('Malam'),
            
        }
        widgets = {
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan Nama Anda','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'noHP': forms.TextInput(attrs={'placeholder': 'Masukkan Nomor Ponsel ','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'email': forms.TextInput(attrs={'placeholder': 'Masukkan Email','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'keluhan_konseling': forms.Textarea(attrs={'placeholder': 'Masukkan keluhan', 'class': 'bg-white rounded-2xl p-4'}),
            'status_user': forms.Select(attrs={'class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'bentuk_konseling': forms.Select(attrs={'class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
        }

        error_messages = {
		    'required' : 'Mohon isi kolom ini',
	    }

# Path: pelayananKonseling\views.py


