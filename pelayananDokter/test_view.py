from django.test import TestCase, Client

from pelayananDokter.views import *
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

    def test_patien(self):
        c = Client()
        User.objects.create(username="test", password='12345')
        data1 = User.objects.get(pk=1)
        Landing.objects.create(user=data1,is_patient=True)
        masuk1 = Landing.objects.get(pk=1)
        self.assertTrue(isPatient(masuk1),True)

    def test_dokter(self):
        c = Client()
        User.objects.create(username="test", password='12345')
        data1 = User.objects.get(pk=1)
        Landing.objects.create(user=data1,is_doctor=True)
        masuk1 = Landing.objects.get(pk=1)
        self.assertTrue(isDoctor(masuk1),True)

    def test_apotek(self):
        c = Client()
        User.objects.create(username="test", password='12345')
        data1 = User.objects.get(pk=1)
        Landing.objects.create(user=data1,is_apotek=True)
        masuk1 = Landing.objects.get(pk=1)
        self.assertTrue(isApotek(masuk1),True)
    
    def test_Admin(self):
        User.objects.create(username="test", password='12345')
        data1 = User.objects.get(pk=1)
        Landing.objects.create(user=data1,is_admin=True)
        masuk1 = Landing.objects.get(pk=1)
        self.assertTrue(isAdmin(masuk1),True)


    def test_keluhan(self):
        self.test1 =  User.objects.create(username="test", password='12345')
        self.landing1 = Landing.objects.create(user=self.test1,is_patient=True)
        self.client.force_login(self.test1)
        r = self.client.get("/pelayananDokter/")
        self.assertEqual(r.status_code, 200)
    
    def test_add(self):
        self.test1 =  User.objects.create(username="test", password='12345')
        self.landing1 = Landing.objects.create(user=self.test1,is_patient=True, is_doctor=True)
        self.client.force_login(self.test1)
        response = self.client.post('/pelayananDokter/add/', {'dokter': self.landing1.pk, 'keluhan': 'makan', 'noHP' : '081298282870'})
        self.assertEqual(response.status_code, 200)

    def test_show(self):
        self.test1 =  User.objects.create(username="test", password='12345')
        self.landing1 = Landing.objects.create(user=self.test1,is_patient=True)
        self.layan1 = Layan.objects.create(user=self.landing1, dokter=self.landing1, keluhan="pusing",noHP="0812"
        , status = False)
        self.client.force_login(self.test1)
        r = self.client.get("/pelayananDokter/show_log/")
        self.assertEqual(r.status_code, 200)