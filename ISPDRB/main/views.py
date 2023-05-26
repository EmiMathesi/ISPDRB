from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import RegisterUserForm, LoginUserForm, UserForm, ProfileForm
from .models import *
from .utils import DataMixin
from django.contrib import messages

# Create your views here.
menu = [
    {'namemenu': 'Главная', 'url_name': 'main'},
    {'namemenu': 'Статьи', 'url_name': 'articles'},
    {'namemenu': 'О проекте', 'url_name': 'about'}
]


def index(request):
    context = {
        'menu': menu,
        'title': 'Природные достопримечательности РБ',
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
    categories = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts,
        'categories': categories
    }
    return render(request, 'main/articles.html', context=context)


def articles_detail(request, article_id):
    posts = Article.objects.filter(pk=article_id)
    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts
    }
    return render(request, 'main/article_detail.html', context=context)


def show_category(request, category_id):
    posts = Article.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts,
        'categories': categories
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


class ShowProfile(DetailView):
    model = Profile
    template_name = 'main/profile.html'


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('update_profile')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'main/update_profile.html', context)

