from django.http import HttpResponse,HttpResponseNotFound,Http404
from django.shortcuts import render, redirect 
from .models import *

# Create your views here.

menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Products", 'url_name': 'products'},
]



def index(request):
    posts = Furnitures.objects.all()
    context =  {
        'posts': posts,
        'menu': menu,
        'title': "main page"
        }
    return render(request, 'furnitures/about.html',context=context)

def about(request):

    return render(request, 'furnitures/index.html', {'title': "about page"})

# def about(request):
#     menu = [
#         {'title': "Home", 'url_name': 'home'},
#         {'title': "Services", 'url_name': 'about'},
#         {'title': "Products", 'url_name': 'products'},
#     ]
#     return render(request, 'index.html', {'menu': menu})

def products(request):
     return render(request, 'furnitures/products.html')


def show_post(request,post_id):
    return  HttpResponse(f'categories page<p>{post_id}<p>')

def categories(request, categ):
    if(request.GET):
        print(requets.GET)
    return HttpResponse(f'categories page<p>{categ}<p>')

def archive (request, year):
    if int(year) > 2025:
        return redirect("home ", permanent=True)
    return HttpResponse(f"<h1>Archive year</h1><p>{year}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>pageNotFound</h1>')