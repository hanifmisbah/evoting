from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
# app_name = 'panitia'
urlpatterns = [
    path('', views.index, name='superadmin'),
    path('agenda/', views.agenda, name='agenda'),
    path('tambah-agenda/', views.tambah_agenda, name='tambah_agenda'),
    path('kandidat/', views.kandidat, name='kandidat'),
    path('tambah-kandidat/', views.tambah_kandidat, name='tambah_kandidat'),
    path('tambah-panitia/', views.tambah_panitia, name='tambah_panitia'),
] 