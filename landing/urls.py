from django.urls import path
from landing.views import change_status, index, menu_pasien, edit_pasien, modif_hasil, show_dokter, show_pasien
from landing.views import login_user, register, logout_user, list_pasien

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

]