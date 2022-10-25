from django.urls import path
from pelayananDokter.views import index

app_name = 'pelayananDokter'

urlpatterns = [
    path('', index, name='index'),
]