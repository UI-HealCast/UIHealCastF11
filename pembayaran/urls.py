from django.urls import path
from . import views
from pembayaran.views import pembayaran, show_receipt_ajax

app_name = 'pembayaran'

urlpatterns = [
    path('pembayaran/', pembayaran, name="pembayaran"),
]