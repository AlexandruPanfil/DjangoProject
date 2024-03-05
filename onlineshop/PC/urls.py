'''Can be different type of data:
str - whatever string symbol without "/"
int - whatever integer number
slug - latin symbols include defis and ...
uuid - latin numbers
path - str with symbol "/" '''


from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('components/<int:components>/', components),  #http:127.0.0.1:8000/PC/components/<components-id>
    path('', my_show, name='home'),  #http:127.0.0.1:8000/PC/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive) #http:127.0.0.1:8000/PC/archive/{year}
]


