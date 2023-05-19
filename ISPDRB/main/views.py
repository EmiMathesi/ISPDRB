from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegisterUserForm
from .models import *
from .utils import DataMixin

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


def login(request):
    context = {
        'menu': menu,
        'title': 'Вход'
    }
    return render(request, 'main/login.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))
