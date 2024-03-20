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
    path('', index, name='home'),  #http:127.0.0.1:8000/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #http:127.0.0.1:8000/archive/{year}
    path('about/', about, name='about'),  #http:127.0.0.1:8000/about/
    path('add_page/', addpage, name='add_page'),   #http:127.0.0.1:8000/add_page/
    path('contact/', contact, name='contact'),   #http:127.0.0.1:8000/contact/
    path('login/', login, name='login'),    #http:127.0.0.1:8000/login/
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
    # path('category/<slug:cat_slug>/', show_category, name='category'),
    ]


