from django.urls import path
from pelayananApotek.views import show_obat
from pelayananApotek.views import add_obat
from pelayananApotek.views import show_obat_json
from pelayananApotek.views import change_status
from pelayananApotek.views import delete_obat
from pelayananApotek.views import change_status_obat

app_name = 'pelayananApotek'

urlpatterns = [
    path('', show_obat, name = 'show_obat'),
    path('add/', add_obat, name = 'add_obat'),
    path('json/', show_obat_json, name='show_obat_json'),
    path('delete_obat/<int:pk>', delete_obat, name='delete_obat'),
    path('change_status/<int:pk>', change_status, name='change_status'),
    path('change_status_obat/<int:pk>', change_status_obat, name='change_status_obat'),
]