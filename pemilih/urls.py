from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select-agenda/', views.aggrement, name='aggrement'),
    path('select-agenda/<agenda_id>/', views.select_agenda, name='select-agenda'),
    path('select-agenda/<agenda_id>/delete', views.cancel_agenda, name='cancel-agenda'),
    path('select-agenda/<agenda_id>/vote/<id>', views.buat_vote, name='buat_vote'),
    path('vote/<id>', views.polls, name='vote'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)