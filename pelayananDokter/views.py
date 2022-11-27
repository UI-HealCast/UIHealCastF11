from http.client import HTTPResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

from pelayananDokter.models import Layan
from landing.models import Landing
from pelayananDokter.forms import LayanForm

# Create your views here.
@login_required(login_url='../../login/')
@csrf_exempt
def addKeluhan(request):
    
    # create object of form
    form = LayanForm()
    form.fields["dokter"].queryset = Landing.objects.filter(is_doctor=True,doctorReady=True)

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
        'statPat' : statusPatient,
        'statDok' : statusDokter,
        'statApo' : statusApotek,
        'statAdm' : statusAdmin,
        'form' : form,
    }
    return render(request, 'layanDokter.html',   context)

def isPatient(masuk):
    if masuk.is_patient:
        return True

def isDoctor(masuk):
    if masuk.is_doctor:
        return True


def doctorReady(masuk):
    data = Landing.objects.filter(doctorReady=True)
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

def isApotek(masuk):
    if masuk.is_apotek:
        return True

def isAdmin(masuk):
    if masuk.is_admin:
        return True

@login_required(login_url='../../login/')
def show_log(request):
    user = request.user
    data = Layan.objects.filter(user = Landing.objects.get(user=user))
    return HttpResponse(serializers.serialize('json', data), content_type='application/json')

@csrf_exempt
def tembakKeluhan(request):
    # check if form data is valid
    if (request.method == 'POST'):
        # save the form data to model
        dokterVal = request.POST.get('dokter')
        dokter = Landing.objects.get(pk=int(dokterVal))
        keluhan = request.POST.get('keluhan')
        noHP = request.POST.get('noHP')
        username = request.user.username
        status = False
        user = Landing.objects.get(user=request.user)
        Layan.objects.create(user=user, dokter=dokter, keluhan=keluhan, noHP = noHP, username=username, status=status, usernameDokter = dokter.username)
        # when saved go back to lab-3
        return JsonResponse({"instance": "Proyek Dibuat"},status=200)
