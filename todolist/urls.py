from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_todo, name='show_todo'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('create-task/', create_task, name='create-task'),
    path('delete/<int:pk>', delete, name='delete'),
    path('change/<int:pk>', change, name='change'),
    path('json/', show_json, name='show_json'),
    path('add/', add_ajax, name='add_ajax'),
]