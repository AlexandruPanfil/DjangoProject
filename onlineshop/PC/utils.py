from django.core.cache import cache

from .models import *


menu = [{'title': "About Site", 'url_name': 'about'},
        {'title': "Add Info", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        # {'title': "Enter", 'url_name': 'login'}
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(self, **kwargs):
        context = kwargs

        cats = Category.objects.all()

        # Here is an exemple of cache, it will save all objects in cache after that will use it for their need

        # cats = cache.get('cats')
        # if not cats:
        #     cats = Category.objects.all()
        #     cache.set('cats', cats, 60)

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats

        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context