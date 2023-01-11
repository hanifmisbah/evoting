from django.contrib import admin
from .models import User, Jurusan
# Register your models here.

class Jurusans(admin.ModelAdmin):
    list_display = ('kode', 'jurusan')
    
class Users(admin.ModelAdmin):
    list_display = ('username', 'jurusan', 'is_panitia', 'is_pemilih')


admin.site.register(User, Users)
admin.site.register(Jurusan, Jurusans)
