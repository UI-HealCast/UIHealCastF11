from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from pelayananApotek.models import Obat
from django.shortcuts import render
from django.http import JsonResponse
from pelayananDokter.models import Layan
from landing.models import Landing
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from pelayananApotek.forms import ObatForm
from django.contrib.auth.models import User
import json

# Create your views here.
def show_obat(request):
    userLogin = Landing.objects.get(user=request.user)
    data_obat = Obat.objects.all().values()
    form = ObatForm()
  
    context = {
        'adalahApotek': userLogin.is_apotek,
        'list_obat' : data_obat,
        'form' : form
    }
    return render(request, "apotek.html", context)

def show_obat_selain_apoteker(request):
    data_obat = Obat.objects.all().values()
    try:
        userLogin = Landing.objects.get(user=request.user)
        if userLogin.is_patient:
            pasien = Layan.objects.get(user=userLogin)
            context = {
                'pasien':pasien,
                'userLogin':userLogin,
                'adalahPasien':userLogin.is_patient,
                'list_obat' : data_obat,
            }
        else:
            context = {
                'userLogin':userLogin,
                'adalahPasien':userLogin.is_patient,
                'list_obat' : data_obat,
            }
    except:
        context = {
            'list_obat' : data_obat,
        }
    return render(request, "apotek_justview.html", context)


def show_obat_json(request):
    data_obat = Obat.objects.all()
    response = serializers.serialize('json', data_obat)
    return HttpResponse(response,content_type='application/json')

@csrf_exempt
def add_obat(request):
    if request.method == 'POST':
        nama_obat = request.POST.get('nama_obat')
        harga = request.POST.get('harga')
        status_obat = True
        description = request.POST.get('description')

        obat = Obat.objects.create(nama_obat=nama_obat,
                    harga=harga,
                    status_obat=status_obat,
                    description=description)
        obat.save()
        result = {
            'fields': {
                'nama_obat': obat.nama_obat,
                'harga': obat.harga,
                'description': obat.description,
                'status_obat': obat.status_obat,
            },
            'pk': obat.pk
        }
        return JsonResponse(result)

def show_patient(request):
    data_pasien = Layan.objects.filter(statusObat=False).values()
    context = {
        'list_pasien' : data_pasien,
    }
    return render(request, "apotek.html", context)

def show_patient_json(request):
    pasien = Layan.objects.filter(statusObat=False)
    response = serializers.serialize("json", pasien)
    return HttpResponse(response, content_type="application/json")

def change_status(request,pk):
    pasien = Layan.objects.get(id=pk)
    pasien.statusObat = not(pasien.statusObat)
    pasien.save()
    return HttpResponse(pasien.statusObat)

@csrf_exempt
def delete_obat(request, pk):
    if request.method == 'DELETE':
        Obat.objects.filter(id=pk).delete()
    return JsonResponse({"instance": "Proyek Dihapus"},status=200)

def delete_obat_flutter(request, pk):
    getObat = Obat.objects.filter(id=pk)
    getObat.delete()
    return HttpResponse(serializers.serialize("json", getObat), content_type="application/json")

def change_status_obat(request, pk):
    obat = Obat.objects.get(id=pk)
    obat.status_obat = not(obat.status_obat)
    obat.save()
    return HttpResponse(obat.status_obat)

def change_status_obat_flutter(request, pk):
    # if request.method == 'POST':
    obat = Obat.objects.get(id=pk)

    obat.status_obat = not(obat.status_obat)
    obat.save()

    return JsonResponse({"status": "success"}, status = 200)

def change_status_pasien_flutter(request, pk):
    # if request.method == 'POST':
    pasien = Layan.objects.get(id=pk)

    pasien.statusObat = not(pasien.statusObat)
    pasien.save()

    return JsonResponse({"status": "success"}, status = 200)


# def get_user(request):
#     userLogin = Landing.objects.get(user=request.user)
#     if userLogin.is_patient:
#         pasien = Layan.objects.get(user=userLogin)
#         return HttpResponse(serializers.serialize("json", pasien), content_type="application/json")
#     else:
#         return JsonResponse({"status": "failed"}, status = 401)
            
    
    # else :
    #     return JsonResponse({"status":"error"}, status = 401)
    #     obat = Obat.objects.get(id=pk)
    #     obat.status_obat = not(obat.status_obat)
    #     obat.save()
    # return JsonResponse({Obat.objects.get(id=pk).status_obat})


# def get_status_obat_pasien(request, username):
#     pasien = Layans.objects.get(username=username)

