from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from python1 import views
urlpatterns = [
    path('',include('python1.urls')),
    path('admin/', admin.site.urls),
]