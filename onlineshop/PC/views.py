import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *

# Create your views here.

menu = [{'title': "About Site", 'url_name': 'about'},
        {'title': "Add Info", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        {'title': "Enter", 'url_name': 'login'}]

class PCHome(ListView):
    model = PC
    template_name = 'PC/index.html'   # if to not give this link so we will have a error, bcz django is looking for {app}/{model_name}_list.html
    context_object_name = 'posts'    # object_list is variable in html file, but in django class is context_object_name
    # extra_context = {'title': 'Main Page',}    #this variable is giving only static context, but for dinamic not as we have menu but we cannot implement it here

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # we are calling super() to not loose the existing data, just to add more
        context['menu'] = menu
        context['title'] = "Main Page"
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return PC.objects.filter(is_published=True)


# def index(requests):
#     posts = PC.objects.all()
#
#     context = {'posts': posts, 'menu': menu, "title": "Main Page", 'cat_selected': 0, }
#
#     return render(requests, 'PC/index.html', context=context)


def about(requests):
    context = {"menu": menu, "title": "About Site"}
    return render(requests, 'PC/about.html', context=context)


# def addpage(requests):
#     if requests.method == 'POST':
#         form = AddPostForm(requests.POST, requests.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(requests, 'pc/addpage.html', {'form': form, 'menu': menu, 'title': 'Adding a new post'})


class AddPage(CreateView):
    # model = PC   # here already is not model, here is form that we created to get data from add_page
    form_class = AddPostForm
    template_name = 'PC/addpage.html'
    success_url = reverse_lazy('home')   # Without this function it will forward me to the post page, but here we are forwarding to 'home'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # we are calling super() to not loose the existing data, just to add more
        context['menu'] = menu
        context['title'] = 'Add Post'
        return context



def contact(requests):
    return HttpResponse(f"<h1>The Contact Page</h1>")


def login(requests):
    return HttpResponse(f"<h1>The Login Page</h1>")


# def show_post(requests, post_slug):
#     post = get_object_or_404(PC, slug=post_slug)
#
#     context = {'post': post, 'menu': menu, 'title': post.title, 'cat_selected': post.cat_id}
#
#     return render(requests, 'PC/post.html', context=context)

class ShowPost(DetailView):
    model = PC
    template_name = 'PC/post.html'
    slug_url_kwarg = 'post_slug'  # if not will be this variable we should call the post via pk or slug, but we want via 'post_slug' to not change everywhere
    context_object_name = 'post'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # we are calling super() to not loose the existing data, just to add more
        context['menu'] = menu
        context['title'] = context['post']
        context['cat_selected'] = 0
        return context

# def show_category(requests, cat_id):
#     posts = PC.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'posts': posts, 'menu': menu, "title": "Show By category", 'cat_selected': cat_id, }
#     return render(requests, 'PC/index.html', context=context)

class PCCategory(ListView):
    model = PC
    template_name = 'PC/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # we are calling super() to not loose the existing data, just to add more
        context['menu'] = menu
        context['title'] = "Category - " + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat_id
        return context

    def get_queryset(self):
        return PC.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)





# def components(request, components):
#     if (request.GET):    #If we have GET Request from the client print GET Request
#         print(request.GET)
#     if (request.POST):   #If we have POST Request from the client print POST Request
#         print(request.POST)
#     return HttpResponse(f"<h1>The Page of Components</h1><p>{components}</p>")
#
# def archive(requests, year):
#     if int(year) > 2020:
#         return redirect('home', permanent=True)
#     return HttpResponse(f"<h1>The Page of Year</h1><p>{year}</p>")

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