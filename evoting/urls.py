from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('panitia/', include('panitia.urls')),
    path('pemilih/', include('pemilih.urls')),
]
