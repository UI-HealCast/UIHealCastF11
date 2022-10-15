from django.urls import path
from example_app.views import index
from example_app.views import login

app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
]