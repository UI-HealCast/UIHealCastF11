from datetime import date
from multiprocessing import context
from django.shortcuts import render

from django.http import HttpResponseRedirect
from landing.models import Landing

from pelayananDokter.models import Layan
from django.shortcuts import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from pelayananDokter.views import isAdmin
from pembayaran.models import Bayar
from django.http import JsonResponse
import json
from pembayaran.forms import DataUser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponseNotFound


# Create your views here.

@login_required(login_url='../../login/')
def show_data(request):
    data_pengguna = Layan.objects.all().values()
    data = Landing.objects.get(user=request.user)
    if data.is_admin:
        context = {
            'list_pengguna' : data_pengguna,
        }
        return render(request, "pembayaran.html", context)
    else:
        data_pengguna = Layan.objects.filter(user=data)
        context = {
            'list_pengguna' : data_pengguna,
        }
        return render(request,  "pembayaranPasien.html", context)

@login_required(login_url='../../login/')
@csrf_exempt
def show_data_json(request):
    data_pengguna = Layan.objects.all()
    response = serializers.serialize('json', data_pengguna)
    return HttpResponse(response,content_type='application/json')

@login_required(login_url='../../login/')
def change_status(request, id):
    change_status = Layan.objects.get(id=id)
    change_status.statusBayar = not(change_status.statusBayar)
    change_status.save()
    return HttpResponseRedirect("/pembayaran")

@login_required(login_url='../../login/')
def show_keterangan(request):
    form = DataUser()
    data = Landing.objects.get(user=request.user)

    context = {
        'form': form,
    }
    return render(request, "keterangan.html", context)

@login_required(login_url='../../login/')
def add_ajax(request):
    if (request.method == 'POST'):
        bulan = request.POST.get('bulan')
        keterangan = request.POST.get('keterangan')

        user = Landing.objects.get(user=request.user)

        Bayar.objects.create(
            user=user,
            bulan=bulan,
            keterangan=keterangan,
        )
        return JsonResponse({"status": "succes"},status=200)


@login_required(login_url='../../login/')
def ket_json(request):
    user = request.user
    data = Bayar.objects.filter(user = Landing.objects.get(user=user))

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
