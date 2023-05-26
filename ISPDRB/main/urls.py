from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('articles/', articles, name='articles'),
    path('articles/<int:article_id>/', articles_detail, name='articles_detail'),
    path('articles/show_category/<int:category_id>/', show_category, name='category'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/<int:pk>/', ShowProfile.as_view(), name='profile'),
    path('update_profile/', update_profile, name='update_profile'),

]
