"""
URL configuration for onlineshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Can be different type of data:
    str - whatever string symbol without "/"
    int - whatever integer number
    slug - latin symbols include defis and ...
    uuid - latin numbers
    path - str with symbol "/"
"""
from django.contrib import admin
from django.urls import path, include
from PC.views import *

# Here we are adding the path of our website, like first you're adding 'link pat/', after that adding the method/class
urlpatterns = [
    path('admin/', admin.site.urls), #http:127.0.0.1:8000/admin/
    path('PC/', include('PC.urls')), #http:127.0.0.1:8000/PC/...
    path('', my_show), #http:127.0.0.1:8000/
]

handler404 = pageNotFound