from django.urls import path
from .views import *

app_name = 'pelayananKonseling'

urlpatterns = [
    path('', addKonseling, name='addKonseling'),
]