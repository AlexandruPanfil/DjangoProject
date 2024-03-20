import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404

from .forms import *
from .models import *

# Create your views here.

menu = [{'title': "About Site", 'url_name': 'about'},
        {'title': "Add Info", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Enter", 'url_name': 'login'}]


def index(requests):
    posts = PC.objects.all()

    context = {'posts': posts, 'menu': menu, "title": "Main Page", 'cat_selected': 0, }

    return render(requests, 'PC/index.html', context=context)


def about(requests):
    context = {"menu": menu, "title": "About Site"}
    return render(requests, 'PC/about.html', context=context)


def addpage(requests):
    if requests.method == 'POST':
        form = AddPostForm(requests.POST, requests.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    return render(requests, 'pc/addpage.html', {'form': form, 'menu': menu, 'title': 'Adding a new post'})


def contact(requests):
    return HttpResponse(f"<h1>The Contact Page</h1>")


def login(requests):
    return HttpResponse(f"<h1>The Login Page</h1>")


def show_post(requests, post_slug):
    post = get_object_or_404(PC, slug=post_slug)

    context = {'post': post, 'menu': menu, 'title': post.title, 'cat_selected': post.cat_id}

    return render(requests, 'PC/post.html', context=context)


def show_category(requests, cat_id):
    posts = PC.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts, 'menu': menu, "title": "Show By category", 'cat_selected': cat_id, }
    return render(requests, 'PC/index.html', context=context)


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