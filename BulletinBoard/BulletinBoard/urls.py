from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Bulletin.urls')),
]
