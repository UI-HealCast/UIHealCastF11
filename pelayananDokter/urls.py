from django.urls import path
from pelayananDokter.views import addKeluhan, tembakKeluhan, show_log,doctorReady

app_name = 'pelayananDokter'

urlpatterns = [
    path('', addKeluhan, name='addKeluhan'),
    path('add/', tembakKeluhan, name='tembakKeluhan'),
    path('show_log/', show_log, name='showLog'),
    path('show_doc/', doctorReady, name='showDoc'),
]