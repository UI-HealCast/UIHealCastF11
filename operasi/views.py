from django.shortcuts import render
from operasi.models import Operasi
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from landing.models import Landing
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from operasi.forms import OperasiForm

# Create your views here.
@login_required(login_url='../../login/')
def show_jadwal_operasi(request):
    userLogin = Landing.objects.get(user=request.user)
    form = OperasiForm()
    form.fields["pasien"].queryset = Landing.objects.filter(is_patient=True)

    context = {
    'adalahDokter': userLogin.is_doctor,
    'form': form
    }
    return render(request, 'jadwaloperasi.html', context)

@csrf_exempt
def add_jadwal_operasi(request):
    if request.method == 'POST':
        dokter = Landing.objects.get(user=request.user)
        pasienVal = request.POST.get('pasien')
        pasien = Landing.objects.get(username=pasienVal)
        tanggal = request.POST.get('tanggal')
        jam = request.POST.get('jam')
        keterangan = request.POST.get('keterangan')

        Operasi.objects.create(dokter = dokter, pasien = pasien,\
                    tanggal = tanggal, jam = jam,\
                    keterangan = keterangan)
        return JsonResponse(status=200)

def jadwal_operasi_json(request):
    userLogin = Landing.objects.get(user=request.user)
    if userLogin.is_doctor:
        data = Operasi.objects.filter(dokter = userLogin)
    elif userLogin.is_patient:
        data = Operasi.objects.filter(pasien = userLogin)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
