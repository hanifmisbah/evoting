from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='panitia'),
    path('base/', views.base, name='base'),
    path('cari', views.cari, name='cari'),
    path('agenda/', views.agenda, name='agenda'),
    path('agenda/<id>/delete', views.agenda_delete),
    path('agenda/<id>/update', views.agenda_update),
    path('tambah_agenda/', views.tambah_agenda, name='tambah_agenda'),
    path('list_kandidat/', views.list_kandidat, name='list_kandidat'),
    path('kandidat/', views.kandidat, name='kandidat'),
    path('kandidat/<id>/delete', views.kandidat_delete, name='delete_kandidat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)