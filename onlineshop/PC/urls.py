from django.urls import path
from .views import *

urlpatterns = [
    path('components/', components),  #http:127.0.0.1:8000/PC/components/
    path('', my_show)  #http:127.0.0.1:8000/PC/
]