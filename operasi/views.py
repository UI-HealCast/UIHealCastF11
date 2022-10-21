from django.shortcuts import render
from operasi.models import Operasi

# Create your views here.
def show_jadwal_operasi(request):
    user = request.user
    # if user.isDoctor():
    #     data = Operasi.objects.filter(dokter = user)
    # else:
    #     data = Operasi.objects.filter(pasien = user)
    data = Operasi.objects.filter(pasien = user) # nanti ini dihapus
    context = {
    'user': user.username,
    'data': data
    }
    return render(request, 'jadwaloperasi.html', context)
