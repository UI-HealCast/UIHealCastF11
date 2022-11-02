from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Obat, Landing

class ObatForm(forms.ModelForm):
    class Meta:
        model = Obat
        fields = ['nama_obat','description','harga']

        nama_obat = forms.CharField(max_length=255)
        description = forms.Textarea()
        harga = forms.IntegerField()

        labels = {
            'nama_obat' : _('Nama Obat'),
            'description' : ('Deskripsi'),
            'harga' : _('Harga'),
        }
        widgets = {
            'nama_obat' : forms.TextInput(attrs={'placeholder': 'Nama Obat','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'description' : forms.TextInput(attrs={'placeholder': 'Deskripsi Obat','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
            'harga' : forms.TextInput(attrs={'placeholder': 'Harga','class': 'form-control', 'class': 'bg-white rounded-2xl p-4'}),
        }
        error_messages = {
            'required' : 'Input cannot be empty'
        }
