from .models import *


menu = [{'title': "About Site", 'url_name': 'about'},
        {'title': "Add Info", 'url_name': 'add_page'},
        {'title': "Feedback", 'url_name': 'contact'},
        # {'title': "Enter", 'url_name': 'login'}
        ]


class DataMixin:
    paginate_by = 3
    def get_user_context(selfself, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context