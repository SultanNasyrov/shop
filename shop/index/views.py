from django.shortcuts import render

from shop.core.views import ShopBaseView
from .models import Banner


class IndexView(ShopBaseView):

    template_name = 'index/index.html'
    page_name = 'Главная страница'

    def change_context(self, request):
        context = self.get_context()
        if Banner.objects.exists():
            context['banner'] = Banner.objects.get()
        return context
