from django import forms

class OperasiForm(forms.Form):
    dokter = forms.CharField(max_length = 100)
    pasien = forms.CharField(max_length = 100)
    tanggal = forms.CharField(max_length = 30)
    jam = forms.CharField(max_length = 30)
    keterangan = forms.Textarea()