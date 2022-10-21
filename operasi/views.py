from django.shortcuts import render
from operasi.models import Operasi
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers

# Create your views here.
def show_jadwal_operasi(request):
    user = request.user
    context = {
    'user': user.username,
    }
    return render(request, 'jadwaloperasi.html', context)

def add_jadwal_operasi(request):
    if request.method == 'POST':
        pasien = request.POST.get('get_pasien')
        jenis = request.POST.get('get_jenis')
        tanggal = request.POST.get('get_tanggal')
        jam = request.POST.get('get_jam')
        durasi = request.POST.get('get_durasi')
        keterangan = request.POST.get('get_keterangan')

        operasi = Operasi(dokter = request.user, pasien = pasien,\
                    jenis = jenis, tanggal = tanggal, jam = jam,\
                    durasi = durasi, keterangan = keterangan)

        operasi.save()
    return render(request, 'jadwaloperasi.html')

def jadwal_operasi_json(request):
    user = request.user
    if user.related_name == 'dokter':
        data = Operasi.objects.filter(dokter = user)
    else:
        data = Operasi.objects.filter(pasien = user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
