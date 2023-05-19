from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('articles/', articles, name='articles'),
    path('login/', login, name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
]
