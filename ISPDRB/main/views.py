from django.shortcuts import render

# Create your views here.

menu = [
    {'namemenu': 'Главная', 'url_name': 'main'},
    {'namemenu': 'Статьи', 'url_name': 'main'},
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