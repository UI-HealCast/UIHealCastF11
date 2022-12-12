from django.urls import path
from pelayananApotek.views import show_obat
from pelayananApotek.views import add_obat
from pelayananApotek.views import show_obat_json
from pelayananApotek.views import change_status
from pelayananApotek.views import delete_obat
from pelayananApotek.views import change_status_obat
from pelayananApotek.views import show_patient_json
from pelayananApotek.views import show_patient
from pelayananApotek.views import show_obat_selain_apoteker
from pelayananApotek.views import delete_obat_flutter
from pelayananApotek.views import change_status_obat_flutter
from pelayananApotek.views import change_status_pasien_flutter

app_name = 'pelayananApotek'

urlpatterns = [
    path('', show_obat, name = 'show_obat'),
    path('add_obat/', add_obat, name = 'add_obat'),
    path('json/', show_obat_json, name='show_obat_json'),
    path('delete_obat/<int:pk>', delete_obat, name='delete_obat'),
    path('change_status/<int:pk>', change_status, name='change_status'),
    path('change_status_obat/<int:pk>', change_status_obat, name='change_status_obat'),
    path('show_patient_json/', show_patient_json, name='show_patient_json'),
    path('show_patient/', show_patient, name='show_patient'),
    path('apotek/', show_obat_selain_apoteker, name='show_obat_selain_apoteker'), 
    path('delete_obat_flutter/<int:pk>', delete_obat_flutter, name='delete_obat_flutter'),
    path('change_status_obat_flutter/<int:pk>', change_status_obat_flutter, name='change_status_obat_flutter'),
    path('change_status_pasien_flutter/<int:pk>', change_status_pasien_flutter, name='change_status_pasien_flutter'),
]