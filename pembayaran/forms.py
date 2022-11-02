# Cek validitas data
from django.utils.translation import gettext_lazy as _
from django import forms 
from pembayaran.models import Bayar

class DataUser(forms.ModelForm):
    class Meta:
        model = Bayar
        fields = ['bulan', 'keterangan']

        labels = {
            'bulan': _('Bulan:'),
            'keterangan': _('Keterangan:'),
        }

        widgets = {
            'bulan': forms.TextInput(attrs={'placeholder': 'Tulis nama bulan','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'keterangan': forms.Textarea(attrs={'placeholder': 'Isi dengan catatan', 'class': 'bg-white rounded-2xl p-4'}),
        }

        error_messages = {
		    'required' : 'Input cannot be empty',
	    }