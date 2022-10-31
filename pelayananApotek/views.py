from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from pelayananApotek.models import Obat
from django.shortcuts import render
from django.http import JsonResponse
from pelayananDokter.models import Layan
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def show_obat(request):
    data_obat = Obat.objects.all().values()
    context = {
        'list_obat' : data_obat,
    }
    return render(request, "apotek.html", context)

def show_obat_json(request):
    data_obat = Obat.objects.all()
    response = serializers.serialize('json', data_obat)
    return HttpResponse(response,content_type='application/json')

def add_obat(request):
    if request.method == 'POST':
        nama_obat = request.POST.get('nama_obat')
        harga = request.POST.get('harga')
        status_obat = True
        description = request.POST.get('description')

        obat = Obat(nama_obat=nama_obat,
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
    data_pasien = Layan.objects.filter(status=False).values()
    context = {
        'list_pasien' : data_pasien,
    }
    return render(request, "apotek.html", context)

def show_patient_json(request):
    pasien = Layan.objects.filter(is_patient=True)
    return HttpResponse(serializers.serialize("json", pasien), content_type="application/json")

def change_status(request,pk):
    pasien = Layan.objects.get(id=pk)
    pasien.statusObat = True
    pasien.save()
    return HttpResponseRedirect(reverse('pelayananApotek:show_patient'))

@csrf_exempt
def delete_obat(request, pk):
    if request.method == 'DELETE':
        Obat.objects.filter(id=pk).delete()
    return JsonResponse({"instance": "Proyek Dihapus"},status=200)

def change_status_obat(request, pk):
    obat = Obat.objects.get(id=pk)
    obat.status_obat = not(obat.status_obat)
    obat.save()
    return HttpResponse(obat.status_obat)


