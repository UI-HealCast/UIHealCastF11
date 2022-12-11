from django.shortcuts import render
from operasi.models import Operasi
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from landing.models import Landing
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from operasi.forms import OperasiForm
from django.contrib.auth.models import User
from itertools import chain
from pelayananDokter.views import isDoctor, isPatient, isApotek, isAdmin
from datetime import datetime

# Create your views here.
@login_required(login_url='../../login/')
def show_jadwal_operasi(request):
    userLogin = Landing.objects.get(user=request.user)
    form = OperasiForm()
    form.fields["pasien"].queryset = Landing.objects.filter(is_patient=True)

    data = Landing.objects.get(user=request.user)
    statusAdmin = False
    statusApotek = False
    statusDokter = False
    statusPatient = False
    if request.user.username != "":
        statusAdmin = isAdmin(data)
        statusApotek = isApotek(data)
        statusDokter = isDoctor(data)
        statusPatient = isPatient(data)

    context = {
        'statPat': statusPatient,
        'statDok': statusDokter,
        'statApo': statusApotek,
        'statAdm': statusAdmin,
        'adalahDokter': userLogin.is_doctor,
        'form': form
    }
    return render(request, 'jadwaloperasi.html', context)


@csrf_exempt
def add_jadwal_operasi(request):
    if request.method == 'POST':
        dokter = Landing.objects.get(user=request.user)
        pasienVal = str(request.POST.get('pasien'))
        pasien = Landing.objects.get(username=pasienVal)
        tanggal = request.POST.get('tanggal')
        if (isinstance(tanggal, str)):
            tanggal = datetime.strptime(tanggal, '%Y-%m-%d')
        jam = request.POST.get('jam')
        if (isinstance(jam, str)):
            jam = datetime.strptime(jam, '%H:%M:%S')
        keterangan = request.POST.get('keterangan')

        Operasi.objects.create(dokter=dokter, usernameDokter=dokter.username, pasien=pasien,
                               usernamePasien=pasien.username, tanggal=tanggal, jam=jam,
                               keterangan=keterangan)
        return JsonResponse({"data": "jadwal"}, status=200)

def jadwal_operasi_json(request):
    userLogin = Landing.objects.get(user=request.user)
    if userLogin.is_doctor:
        data = Operasi.objects.filter(dokter=userLogin)
    elif userLogin.is_patient:
        data = Operasi.objects.filter(pasien=userLogin)
    return HttpResponse(serializers.serialize("json", data.order_by('tanggal', 'jam')), content_type="application/json")

def list_pasien_json(request):
    data = Landing.objects.filter(is_patient=True)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


@csrf_exempt
def delete_operasi(request, pk):
    getOperasi = Operasi.objects.filter(pk=pk)
    getOperasi.delete()
    return show_jadwal_operasi(request)

@csrf_exempt
def delete_operasi_flutter(request, pk):
    getOperasi = Operasi.objects.filter(pk=pk)
    getOperasi.delete()
    return HttpResponse(serializers.serialize("json", getOperasi), content_type="application/json")
