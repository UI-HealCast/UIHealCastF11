from django.urls import path
from pelayananDokter.views import addKeluhan, tembakKeluhan

app_name = 'pelayananDokter'

urlpatterns = [
    path('', addKeluhan, name='addKeluhan'),
    path('add/', tembakKeluhan, name='tembakKeluhan'),
]