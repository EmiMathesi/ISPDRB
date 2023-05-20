from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, TemplateView

from .forms import RegisterUserForm, LoginUserForm
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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_lict=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


class ShowProfile(TemplateView):
    model = Profile
    template_name = 'main/profile.html'

    def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


