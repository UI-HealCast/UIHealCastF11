from django.utils.translation import gettext_lazy as _
from django import forms    
from .models import Layan, Landing

# https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django


# CurhatForm class for views
class DateInput(forms.DateTimeInput):
    input_type = 'date'

class LayanForm(forms.ModelForm):

    class Meta:
        model = Layan
        fields=['dokter','keluhan', 'noHP']


        dokter = forms.ModelChoiceField(queryset=Landing.objects.filter(is_doctor=True))
        noHP = forms.CharField(max_length=50, required=True)
        keluhan = forms.Textarea()

        labels = {
            'dokter': _('Pilih Dokter'),
            'keluhan': _('Isi keluhan'),
            'noHP': _('Masukkan nomor yang dapat dihubungi'),
        }
        widgets = {
            'keluhan': forms.Textarea(attrs={'placeholder': 'Masukkan keluhan', 'class': 'bg-white rounded-2xl p-4'}),
        }

        error_messages = {
		    'required' : 'Input cannot be empty',
	    }

