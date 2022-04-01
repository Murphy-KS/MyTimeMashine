"""

MyTimeMaschine URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from polls import urls as pollurl



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pollurl)),
]
