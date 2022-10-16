from django.urls import path
from main.views import index
from main.views import login, register, logout_user

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]