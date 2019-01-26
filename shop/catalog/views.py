from django.shortcuts import render, HttpResponse

from shop.core.views import ShopBaseView

from .models import Product

import json


class IndexView(ShopBaseView):
    """Главная страница каталога"""

    page_name = 'Каталог: главная'
    template_name = 'catalog/index.html'

    def change_context(self, request):
        context = self.get_context()
        return context

