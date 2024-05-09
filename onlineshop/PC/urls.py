'''Can be different type of data:
str - whatever string symbol without "/"
int - whatever integer number
slug - latin symbols include defis and ...
uuid - latin numbers
path - str with symbol "/" '''


from django.urls import path, re_path, include
from .views import *



urlpatterns = [
    #path('components/<int:components>/', components),  #http:127.0.0.1:8000/PC/components/<components-id>
    path('', PCHome.as_view(), name='home'),  #http:127.0.0.1:8000/
    #re_path(r'^archive/(?P<year>[0-9]{4})/', archive), #http:127.0.0.1:8000/archive/{year}
    path('about/', about, name='about'),  #http:127.0.0.1:8000/about/
    path('add_page/', AddPage.as_view(), name='add_page'),   #http:127.0.0.1:8000/add_page/
    path('contact/', contact, name='contact'),   #http:127.0.0.1:8000/contact/
    path('login/', LoginUser.as_view(), name='login'),    #http:127.0.0.1:8000/login/
    path('register/', Register.as_view(), name='register'),    #http:127.0.0.1:8000/register/
    path('logout/', logout_user, name='logout'),    #http:127.0.0.1:8000/logout/
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),    #http:127.0.0.1:8000/post/{slug}
    path('category/<slug:cat_slug>/', PCCategory.as_view(), name='category'),    #http:127.0.0.1:8000/category/{slug}
    ]


