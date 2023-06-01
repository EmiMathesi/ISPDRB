from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .forms import RegisterUserForm, LoginUserForm, UserForm, ProfileForm, AddCommentForm
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
        'title': 'Природные достопримечательности РБ',
    }
    return render(request, 'main/index.html', context=context)


def articles(request):
    posts = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'main/articles.html', context=context)


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


def articles_detail(request, article_id):
    posts = get_object_or_404(Article, id=article_id)
    comments = Comments.objects.filter(article_id=article_id)
    categories = Category.objects.all()
    if request.method == 'POST':
        comments_form = AddCommentForm(request.POST)
        if comments_form.is_valid():
            new_comment = comments_form.save(commit=False)
            new_comment.article = posts
            new_comment.autor = request.user
            new_comment.save()
            return redirect('articles')

    else:
        comments_form = AddCommentForm()

    context = {
        'menu': menu,
        'title': 'Статьи',
        'posts': posts,
        'categories': categories,
        'comments': comments,
        'comments_form': comments_form,
    }
    return render(request, 'main/article_detail.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О проекте'
    }
    return render(request, 'main/about.html', context=context)


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
        'menu': menu,
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'main/update_profile.html', context)

