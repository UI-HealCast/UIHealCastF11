from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from landing.models import Landing
from .forms import *


# Create your views here.

@login_required(login_url='../../login/')
def addKonseling(request):
    pelayanan_konseling_form = PelayananKonselingForm()
    preferensi_hari_form = PreferensiHariForm()
    preferensi_waktu_form = PreferensiWaktuForm()

    context = {
        'pelayanan_konseling_form': pelayanan_konseling_form,
        'preferensi_hari_form': preferensi_hari_form,
        'preferensi_waktu_form': preferensi_waktu_form,
    }
    return render(request, 'addKonseling.html', context)
