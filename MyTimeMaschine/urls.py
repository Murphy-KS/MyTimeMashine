"""

MyTimeMaschine URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from timerecorder import urls as time_app



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(time_app)),
]
