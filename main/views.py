from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
import datetime
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect

def index(request):
    user = request.user
    status = False
    if (user):
        status = True
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("main:index")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('main:index')
    
    context = {'form':form}
    return render(request, 'register.html', context)