from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('superadmin/', include('superuser.urls')),
    path('panitia/', include('panitia.urls')),
    path('pemilih/', include('pemilih.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
