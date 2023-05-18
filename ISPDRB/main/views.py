from django.shortcuts import render
from .models import *
# Create your views here.

menu = [
    {'namemenu': 'Главная', 'url_name': 'main'},
    {'namemenu': 'Статьи', 'url_name': 'articles'},
    {'namemenu': 'О проекте', 'url_name': 'about'}
]
def index(request):
    context = {
        'menu': menu,
        'title': 'Природные достопримечательности РБ'
    }
    return render(request, 'main/index.html', context=context)

def about(request):
    context = {
        'menu': menu,
        'title': 'О проекте'
    }
    return render(request, 'main/about.html', context=context)

def articles(request):
    posts = Article.objects.all()
    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts
    }
    return render(request, 'main/articles.html', context=context)