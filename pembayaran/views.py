from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pembayaran.models import Order
import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.http import HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from pelayananDokter.models import Layan
from django.shortcuts import HttpResponse

# Create your views here.

# @csrf_exempt
# def change_status(request):
#      if request.method == "PATCH":
#         task = Layan.objects.get(user=request.user)
#         task.doctorReady = not (task.doctorReady)
#         task.save()
#         return JsonResponse({"instance": "Proyek Dibuat"},status=200)

def change_status(request,pk):
    bayar = Layan.objects.get(id=pk)
    bayar.statusBayar = not(bayar.statusBayar)
    bayar.save()
    return HttpResponse(bayar.statusBayar)


def change_status(request, id):
    bayar = Layan.objects.get(id=id)
    if change_status.is_finished:
        change_status.is_finished = False
    else:
        change_status.is_finished = True
    change_status.save()
    return HttpResponseRedirect("/todolist")