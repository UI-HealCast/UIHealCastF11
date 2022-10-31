from django.urls import path
from .views import *

app_name = 'pelayananKonseling'

urlpatterns = [
    path('', addKonseling, name='addKonseling'),
    path('tembakDBAjax/', tembakDBAjax, name='tembakDBAjax'),
    path('show_json_konseling/', show_json_konseling, name='show_json_konseling'),
]