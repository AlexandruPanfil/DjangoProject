import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .models import *

# Create your views here.

menu = ["About Site", "Add Info", "Feedback", "Enter"]

def index(requests):
    posts = PC.objects.all()
    return render(requests, 'PC/index.html', {'posts':posts, 'menu': menu, "Title": "Main Page"})

def about(requests):
    return render(requests, 'PC/about.html', {"menu": menu, "Title": "About Site"})

def components(request, components):
    if (request.GET):    #If we have GET Request from the client print GET Request
        print(request.GET)
    if (request.POST):   #If we have POST Request from the client print POST Request
        print(request.POST)
    return HttpResponse(f"<h1>The Page of Components</h1><p>{components}</p>")

def archive(requests, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>The Page of Year</h1><p>{year}</p>")

# Return error page not found
# def archive(requests, year):
#     if int(year) > 2020:
#         raise Http404()
#         # handler 404 - Page not found
#         # handler 500 - Server Error
#         # handler 403 - Limited access
#         # handler 400 - Can't process the request

#     return HttpResponse(f"<h1>The Page of Year</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>The Page Is Not Found<h1>")