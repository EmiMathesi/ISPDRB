menu = [
    {'namemenu': 'Главная', 'url_name': 'main'},
    {'namemenu': 'Статьи', 'url_name': 'articles'},
    {'namemenu': 'О проекте', 'url_name': 'about'},
    {'namemenu': 'Зарегистрироваться', 'url_name': 'login'}
]


class DataMixin:
    def get_user_context(self, **kwargs):
        pass
