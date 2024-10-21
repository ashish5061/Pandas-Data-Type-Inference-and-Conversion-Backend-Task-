from django.urls import path
from .views import upload_file,overrideDataType
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('api/upload', upload_file, name='upload_file'),
    path('api/override', overrideDataType, name='override_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
