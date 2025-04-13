from django.urls import path, include 
from django.contrib import admin

urlpatterns = [
    path('auth/', include('djoser.urls')),  
    path('auth/', include('djoser.urls.authtoken')), 
]