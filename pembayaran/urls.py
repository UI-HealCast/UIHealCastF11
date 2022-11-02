from django.urls import path
from pembayaran.views import show_data, show_data_json, change_status, add_ajax, show_keterangan, ket_json

app_name = 'pembayaran'

urlpatterns = [
    path('', show_data, name='show_data'),
    path('json/', show_data_json, name='show_data_json'),
    path('change_status/<int:id>', change_status, name='change_status'),
    path('keterangan/', show_keterangan, name='show_keterangan'),
    path('keterangan/add/', add_ajax, name='add_ajax'),
    path('keterangan/json/', ket_json, name='ket_json')
]