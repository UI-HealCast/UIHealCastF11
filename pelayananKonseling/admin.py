from django.contrib import admin
from .models import *

# Register your models here.
class PelayananKonselingAdmin(admin.ModelAdmin):
    list_display = ('nama', 'status_user', 'noHP', 'email', 'bentuk_konseling', 'username', 'status_konseling')
    search_fields = ('nama', 'status_user', 'noHP', 'email', 'bentuk_konseling', 'username', 'status_konseling')
    list_filter = ('status_user', 'bentuk_konseling', 'status_konseling')


admin.site.register(PelayananKonseling, PelayananKonselingAdmin)
