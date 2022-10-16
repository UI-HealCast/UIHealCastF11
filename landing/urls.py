from django.urls import path
from landing.views import index
from landing.views import login_user, register, logout_user

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
]