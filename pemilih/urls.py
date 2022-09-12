from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index),
    path('<id>/data', views.showdatakandidat, name='showdata'),
    path('vote/<id>', views.vote, name='vote'),
    # path('<id>/show_kandidat', views.show_kandidat, name='show'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
