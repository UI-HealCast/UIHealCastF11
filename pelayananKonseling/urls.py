from django.urls import path
from .views import *

app_name = 'pelayananKonseling'

urlpatterns = [
    path('', addKonseling, name='addKonseling'),
    path('tembakDBAjax/', tembakDBAjax, name='tembakDBAjax'),
    path('show_json_konseling/', show_json_konseling, name='show_json_konseling'),
    path('show_json_konseling_dokter/', show_json_konseling_dokter, name='show_json_konseling_dokter'),
    path('set-konseling/<int:pk>', ubah_status, name='ubah_status'),
    path('delete/<int:pk>', hapus, name='hapus'),
]