from django.urls import path
from operasi.views import show_jadwal_operasi

app_name = 'operasi'

urlpatterns = [
    path('', show_jadwal_operasi, name='show_jadwal_operasi'),
]