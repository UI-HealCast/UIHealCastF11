from django.test import TestCase, Client

from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .models import PelayananKonseling
from landing.models import Landing
from .views import *
from django.utils.encoding import force_str

# Create your tests here.
class TestViewKonseling(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        self.landing = Landing.objects.create(user=self.user, is_patient=True)
        
        self.pelayananKonseling = PelayananKonseling.objects.create(
            user = self.landing,
            username = self.landing.username,
            status_user = "Mahasiswa UI",
            noHP = 23423423432,
            email = "test@email.com",
            bentuk_konseling = "Offline",
            keluhan_konseling = "test",
            status_konseling = False,
            senin = True,
            pagi = True
        )
        # self.pelayananKonseling.save()
        self.login = self.client.login(username='testuser', password='12345')

    def test_show_konseling(self):
        response = self.client.get(reverse('pelayananKonseling:addKonseling'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'addKonseling.html')

    def test_show_json_konseling(self):
        response = self.client.get(reverse('pelayananKonseling:show_json_konseling'))
        self.assertEqual(response.status_code, 200)
      
    def test_add_konseling(self):
        response = self.client.post(reverse('pelayananKonseling:addKonseling'), {
            'username': self.landing.username,
            'status_user': "Mahasiswa UI",
            'noHP': 23423423432,
            'email': "aa@gmail.com"
        })
        self.assertEqual(response.status_code, 200)

    def test_model_konseling(self):
        self.assertEqual(self.pelayananKonseling.username, self.landing.username)
        self.assertEqual(self.pelayananKonseling.status_user, "Mahasiswa UI")
        self.assertEqual(self.pelayananKonseling.noHP, 23423423432)
        self.assertEqual(self.pelayananKonseling.email, "test@email.com")
        self.assertEqual(self.pelayananKonseling.bentuk_konseling, "Offline")
        self.assertEqual(self.pelayananKonseling.keluhan_konseling, "test")
        self.assertEqual(self.pelayananKonseling.status_konseling, False)
        self.assertEqual(self.pelayananKonseling.senin, True)
        self.assertEqual(self.pelayananKonseling.pagi, True)

    def test_url_konseling(self):
        response = self.client.get('/pelayananKonseling/')
        self.assertEqual(response.status_code, 200)

    def test_add_konseling(self):
        response = self.client.post(reverse('pelayananKonseling:addKonseling'), {
            'username': self.landing.username,
            'status_user': "Mahasiswa UI",
            'noHP': 23423423432,
            'email': "test@email.com",
            'bentuk_konseling': "Offline",
            'keluhan_konseling': "test",
            'status_konseling': False,
            'senin': True,
            'pagi': True
        })
        self.assertEqual(response.status_code, 200)

    def test_json_response(self):
        response = self.client.get(reverse('pelayananKonseling:show_json_konseling'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
    
    def test_show_konseling2(self):
        url = reverse('pelayananKonseling:addKonseling')
        self.assertEquals(resolve(url).func, addKonseling)
        
    def test_str_models(self):
        str_rep = self.pelayananKonseling.__str__()
        self.assertEqual(str_rep, self.pelayananKonseling.nama)

    def test_AJAX_POST(self):
        response = self.client.post(reverse('pelayananKonseling:tembakDBAjax'), {
            'username': self.landing.username,
            'nama': "test",
            'status_user': "Mahasiswa UI",
            'noHP': 23423423432,
            'email': "test@email.com",
            'bentuk_konseling': "Offline",
            'keluhan_konseling': "test",
            'status_konseling': False,
            'senin': True,
            'selasa': True,
            'rabu': True,
            'kamis': True,
            'jumat': True,
            'sabtu': True,
            'minggu': True,
            'pagi': True,
            'siang': True,
            'sore': True,
            'malam': True
        })
    
        self.assertEqual(response.status_code, 200)

        response_content = response.content.decode('utf-8')
        self.assertJSONEqual(response_content, {"status": "succes"})

    



    
