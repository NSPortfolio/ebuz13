from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib import admin
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.indexpage),
    path('home/', views.homepage),
    path('mywebsites/', views.websites),
    path('amandasbakery/create/', views.example),
    path('searchforstartups/bakeries/', views.search),
]