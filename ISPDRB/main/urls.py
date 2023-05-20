from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('about/', about, name='about'),
    path('articles/', articles, name='articles'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', ShowProfile.as_view(), name='profile'),
    path('register/', RegisterUser.as_view(), name='register'),
]
