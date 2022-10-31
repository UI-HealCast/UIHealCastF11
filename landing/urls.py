from django.urls import path
from landing.views import *

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('list-pasien/', list_pasien, name='listPasien'),
    path('menu-pasien/', menu_pasien, name='menuPasien'),
    path('menu-pasien/edit/<int:pk>', edit_pasien, name='editPasien'),
    path('show-pasien/<int:pk>', show_pasien, name='showPasien'),
    path('show-dokter/', show_dokter, name='showDokter'),
    path('change-status/', change_status, name='changeStatus'),
    path('modif-hasil/', modif_hasil, name='modifHasil'),
    path('show_json_konseling_dokter/', show_json_konseling_dokter, name='show_json_konseling_dokter'),
    path('menu-pasien/set-konseling/<int:pk>', ubah_status, name='ubah_status'),
    path('menu-pasien/delete/<int:pk>', hapus, name='hapus'),   
]