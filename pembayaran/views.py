from django.shortcuts import render

from django.http import HttpResponseRedirect

from pelayananDokter.models import Layan
from django.shortcuts import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='../../login/')
def show_data(request):
    data_pengguna = Layan.objects.all().values()
    context = {
        'list_pengguna' : data_pengguna,
    }
    return render(request, "pembayaran.html", context)

def show_data_json(request):
    data_pengguna = Layan.objects.all()
    response = serializers.serialize('json', data_pengguna)
    return HttpResponse(response,content_type='application/json')

def change_status(request, id):
    change_status = Layan.objects.get(id=id)
    change_status.statusBayar = not(change_status.statusBayar)
    change_status.save()
    return HttpResponseRedirect("/pembayaran")