from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from landing.models import Landing
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.contrib.auth.models import User
from pelayananDokter.models import Layan
from django.core import serializers
from django.http.response import JsonResponse, HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from pelayananKonseling.models import PelayananKonseling


def index(request):
    masuk = None
    statusAdmin = False
    statusApotek = False
    statusDokter = False
    statusPatient = False
    if request.user.username != "":
        masuk = getUser(request.user)
        statusAdmin = isAdmin(masuk)
        statusApotek = isApotek(masuk)
        statusDokter = isDoctor(masuk)
        statusPatient = isPatient(masuk)
    context = {
    'statPat' : statusPatient,
    'statDok' : statusDokter,
    'statApo' : statusApotek,
    'statAdm' : statusAdmin,
    'user': request.user.username,
    'nama': 'Yudi Putra Sabri',
    'npm': 2106706123,
    }
    return render(request, 'index.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("landing:index")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!"
            # Insert any extra data if you want to pass data to Flutter
            }, status=200)
        else:
            messages.info(request, 'Username atau Password salah!')
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, check your email/password."
            }, status=401)
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        uname = request.POST.get('username')
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            getUs = User.objects.get(username=uname)
            Landing.objects.create(user=getUs, is_patient=True, username=getUs.username)
            return redirect('landing:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('landing:index'))
    response.delete_cookie('last_login')
    return response

def isPatient(masuk):
    if masuk.is_patient:
        return True

def isDoctor(masuk):
    if masuk.is_doctor:
        return True

def isApotek(masuk):
    if masuk.is_apotek:
        return True

def isAdmin(masuk):
    if masuk.is_admin:
        return True

def getUser(test):
    return Landing.objects.get(user=test.pk)

def list_pasien(request):
    data = Landing.objects.get(user=request.user)
    if data.is_doctor:
        data = Layan.objects.filter(hasilPeriksa="-",dokter=data)
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    else:
        return HttpResponseNotFound("You Don't Belong Here")
        
@login_required(login_url='../../login/')
def menu_pasien(request):
    data = Landing.objects.get(user=request.user)
    if data.is_doctor:
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
            'statPat' : statusPatient,
            'statDok' : statusDokter,
            'statApo' : statusApotek,
            'statAdm' : statusAdmin,
            'ready' : data.doctorReady,
        }
        return render(request, 'menuPasien.html', context)
    else:
        return HttpResponseNotFound("You Don't Belong Here")  

def edit_pasien(request, pk):
    data = Landing.objects.get(user=request.user)
    dataPasien = Landing.objects.filter(pk=pk)
    if data.is_doctor:
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
            'statPat' : statusPatient,
            'statDok' : statusDokter,
            'statApo' : statusApotek,
            'statAdm' : statusAdmin,
            'pasien'  : dataPasien,
            'masuk' : pk,
        }
    return render(request, 'editPasien.html', context)

def show_pasien(request, pk):
    data = Landing.objects.get(user=request.user)
    if data.is_doctor:
        data = Layan.objects.filter(pk=pk)
        return HttpResponse(serializers.serialize('json', data), content_type='application/json')
    else:
        return HttpResponseNotFound("You Don't Belong Here")  

def show_dokter(request):
    data = Landing.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@csrf_exempt
def change_status(request):
     if request.method == "PATCH":
        task = Landing.objects.get(user=request.user)
        task.doctorReady = not (task.doctorReady)
        task.save()
        return JsonResponse({"instance": "Proyek Dibuat"},status=200)

@csrf_exempt
def modif_hasil(request):
    if request.method == 'POST':
        desc = request.POST.get('hasil')
        peka = request.POST.get('peka')
        dataMasuk = Layan.objects.get(pk=peka)
        dataMasuk.hasilPeriksa = desc
        dataMasuk.status = not dataMasuk.status
        dataMasuk.save()
        return JsonResponse({"instance": "Proyek Dibuat"},status=200)

@login_required(login_url='../../login/')
def show_json_konseling_dokter(request):
    data = PelayananKonseling.objects.all()
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def ubah_status(request, pk):
    data = PelayananKonseling.objects.get(pk=pk)
    data.status_konseling = not data.status_konseling
    data.save()
    return redirect('landing:menuPasien')

def hapus(request, pk):
    data = PelayananKonseling.objects.get(id=pk)
    data.delete()
    return JsonResponse({'status': 'success'})
