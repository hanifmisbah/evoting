from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
# app_name = 'panitia'
urlpatterns = [
    path('', index, name='panitia'),
    path('select-info/<id>', info_kandidat, name='info_kandidat'),
    path('agenda/', agenda, name='agenda'),
    path('agenda/kandidatfilter/<id>', kandidatfilter, name='kandidatfilter'), #hasil voting
    path('agenda/<id>/delete', agenda_delete, name='delete_agenda'),
    path('agenda/<id>/update', agenda_update, name='update_agenda'),
    path('tambah_agenda/', tambah_agenda, name='tambah_agenda'),
    path('list_kandidat/', list_kandidat, name='list_kandidat'),
    path('kandidat/', kandidat, name='kandidat'),
    path('kandidat/<id>/delete', kandidat_delete, name='delete_kandidat'),
    path('kandidat/<id>/update', kandidat_update, name='update_kandidat'),
    path('data_pemilih/', pemilih, name='data_pemilih'),
    path('tambah_pemilih/', regisPemilih, name='regis_pemilih'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)