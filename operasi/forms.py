from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Operasi, Landing

class DateInput(forms.DateTimeInput):
    input_type = 'date'

class OperasiForm(forms.ModelForm):
    class Meta:
        model = Operasi
        fields = ['dokter', 'pasien', 'tanggal', 'jam', 'keterangan']

        pasien = forms.ModelChoiceField(queryset=Landing.objects.filter(is_patient=True))
        tanggal = forms.CharField(max_length = 30, required=True)
        jam = forms.CharField(max_length = 30, required=True)
        keterangan = forms.Textarea()

        labels = {
            'pasien': _('Username Pasien'),
            'tanggal': _('Tanggal Operasi'),
            'jam': _('Jam Operasi'),
            'keterangan': _('Keterangan')
        }
        widgets = {
            'keterangan': forms.Textarea(attrs={'class': 'bg-white rounded-2xl p-4'})
        }

        error_messages = {
		    'required' : 'Input cannot be empty'
	    }
