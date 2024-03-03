from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>The page of PC<h1>")

def my_show(requests):
    return HttpResponse("<h1>The Main Page<h1>")

def components(requests):
    return HttpResponse("<h1>The Page of Components<h1>")