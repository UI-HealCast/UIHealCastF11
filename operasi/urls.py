from django.urls import path
from operasi.views import show_jadwal_operasi, jadwal_operasi_json, add_jadwal_operasi

app_name = 'operasi'

urlpatterns = [
    path('', show_jadwal_operasi, name='show_jadwal_operasi'),
    path('json/', jadwal_operasi_json, name='jadwal_operasi_json'),
    path('add/', add_jadwal_operasi, name='add_jadwal_operasi')
]