from django.test import TestCase
from operasi.views import show_jadwal_operasi
from django.urls import reverse, resolve

class OperasiTest(TestCase):
    def test_show_jadwal(self):
        url = reverse("operasi:show_jadwal_operasi")
        self.assertEquals(resolve(url).func,show_jadwal_operasi)

    
