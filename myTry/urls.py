from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.homepage, name='home'),
    path('count/', views.count, name='count'),
    path('aboutus/', views.about_us, name='about'),
]

