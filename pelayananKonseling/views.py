from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from landing.models import Landing
from .forms import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@login_required(login_url='../../login/')
def addKonseling(request):
    pelayanan_konseling_form = PelayananKonselingForm()

    context = {
        'pelayanan_konseling_form': pelayanan_konseling_form,
    }
    return render(request, 'addKonseling.html', context)

@csrf_exempt
def tembakDBAjax(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        status_user = request.POST.get('status_user')
        noHP = request.POST.get('noHP')
        email = request.POST.get('email')
        bentuk_konseling = request.POST.get('bentuk_konseling')
        keluhan_konseling = request.POST.get('keluhan_konseling')
        user = Landing.objects.get(user=request.user)
        username = request.user.username
        status_konseling = False
        
        senin = request.POST.get('senin')
        selasa = request.POST.get('selasa')
        rabu = request.POST.get('rabu')
        kamis = request.POST.get('kamis')
        jumat = request.POST.get('jumat')
        sabtu = request.POST.get('sabtu')
        minggu = request.POST.get('minggu')

        pagi = request.POST.get('pagi')
        siang = request.POST.get('siang')
        sore = request.POST.get('sore')
        malam = request.POST.get('malam')

        if senin == 'on':
            senin = True
        else:
            senin = False

        if selasa == 'on':
            selasa = True
        else:
            selasa = False

        if rabu == 'on':
            rabu = True
        else:
            rabu = False

        if kamis == 'on':
            kamis = True
        else:
            kamis = False

        if jumat == 'on':
            jumat = True
        else:
            jumat = False

        if sabtu == 'on':
            sabtu = True
        else:
            sabtu = False

        if minggu == 'on':
            minggu = True
        else:
            minggu = False

        if pagi == 'on':
            pagi = True
        else:
            pagi = False

        if siang == 'on':
            siang = True
        else:
            siang = False

        if sore == 'on':
            sore = True
        else:
            sore = False

        if malam == 'on':
            malam = True
        else:
            malam = False

        PelayananKonseling.objects.create(
            user=user,
            nama=nama,
            status_user=status_user,
            noHP=noHP,
            email=email,
            bentuk_konseling=bentuk_konseling,
            keluhan_konseling=keluhan_konseling,
            status_konseling=status_konseling,
            senin=senin,
            selasa=selasa,
            rabu=rabu,
            kamis=kamis,
            jumat=jumat,
            sabtu=sabtu,
            minggu=minggu,
            pagi=pagi,
            siang=siang,
            sore=sore,
            malam=malam,
        )

        return JsonResponse({"data": "succes"},status=200)