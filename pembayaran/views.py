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


# Create your views here.

@login_required(login_url='../../login/')
def show_data(request):
    data_pengguna = Layan.objects.all().values()
    context = {
        'list_pengguna' : data_pengguna,
    }
    return render(request, "pembayaran.html", context)

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

# update
# @login_required(login_url='../../login/')
# def get_bulan_ket(request):
#     user = request.user
#     get = Bayar.objects.filter(user = Landing.objects.get(user=user))

#     context = {
#         'bulan': get.bulan,
#         'keterangan': get.keterangan,
#     }
#     return render(request, "keterangan.html", context)

@login_required(login_url='../../login/')
def add_ajax(request):
    # check if form data is valid
    if (request.method == 'POST'):
        # save the form data to model
        bulan = request.POST.get('bulan')
        keterangan = request.POST.get('keterangan')

        user = Landing.objects.get(user=request.user)
        # bayar_new = Bayar.objects.create(user=user, bulan=bulan, keterangan=keterangan)
        # bayar_new.save()
            
        # bayar = {'bulan': bayar_new.bulan, 'keterangan': bayar_new.keterangan}

        # dt = {
        #     'bayar': bayar,
        #     'url': 'pembayaran/keterangan'
        # }

        Bayar.objects.create(
            user=user,
            bulan=bulan,
            keterangan=keterangan,
        )
        # when saved go back to lab-3
        # print("sebelum return")
        # return JsonResponse(dt)
        return JsonResponse({"status": "succes"},status=200)


@login_required(login_url='../../login/')
def ket_json(request):
    user = request.user
    data = Bayar.objects.filter(user = Landing.objects.get(user=user))

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# update
# @login_required(login_url='../../login/')
# def show_list(request):
#     data_ket = Bayar.objects.all()
#     context = {
#         'list_ket' : data_ket
#     }
#     return render(request, "keterangan.html", context)
