from django.shortcuts import render, HttpResponse, get_object_or_404

from shop.core.views import ShopBaseView

from .models import Product

import json


class IndexView(ShopBaseView):
    """Главная страница каталога"""

    page_name = 'Каталог: главная'
    template_name = 'catalog/index.html'

    def prepare_context(self, request, args, kwargs):
        print('Catalog:Index view get change context')
        context = self.get_context()
        context['products'] = Product.displayed.all()
        return context




