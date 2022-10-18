from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
# app_name = 'panitia'
urlpatterns = [
    path('', views.index, name='panitia'),
    # path('<id>', views.index,),
    path('cari', views.cari, name='cari'),
    path('agenda/', views.agenda, name='agenda'),
    path('agenda/agendafilter', views.agendafilter, name='agendafilter'), #hasil render agenda
    path('agenda/kandidatfilter/<id>', views.kandidatfilter, name='kandidatfilter'), #hasil voting
    path('agenda/<id>/delete', views.agenda_delete, name='delete_agenda'),
    path('agenda/<id>/update', views.agenda_update, name='update_agenda'),
    path('tambah_agenda/', views.tambah_agenda, name='tambah_agenda'),
    path('list_kandidat/', views.list_kandidat, name='list_kandidat'),
    path('kandidat/', views.kandidat, name='kandidat'),
    path('kandidat/<id>/delete', views.kandidat_delete, name='delete_kandidat'),
    path('kandidat/<id>/update', views.kandidat_update, name='update_kandidat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)