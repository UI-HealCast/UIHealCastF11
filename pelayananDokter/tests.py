from django.test import TestCase, Client

from pelayananDokter.views import addKeluhan
from .models import Landing, Layan
from django.contrib.auth.models import User
from django.urls import reverse, resolve

class TestViews(TestCase):
    def test_models(self):
        User.objects.create(username="test", password='12345')
        User.objects.create(username="test1", password='12345')

        data1 = User.objects.get(pk=1)
        data2 = User.objects.get(pk=2)

        Landing.objects.create(user=data1,is_patient=True)
        Landing.objects.create(user=data2,is_doctor=True, doctorReady=True)

        masuk1 = Landing.objects.get(pk=1)
        masuk2 = Landing.objects.get(pk=2)

        Layan.objects.create(user=masuk1, dokter=masuk2, keluhan="pusing",noHP="0812"
        , status = False)
        data = Layan.objects.get(user=masuk1)

        self.assertEquals(data.keluhan,"pusing")

    def test_view(self):
        url = reverse("pelayananDokter:addKeluhan")
        self.assertEquals(resolve(url).func,addKeluhan)

    def test_login(self):
        client = Client()
        response = client.post("/login/",{'username' : 'test', 'password' : '12345'})
        self.assertEquals(response.status_code,200)