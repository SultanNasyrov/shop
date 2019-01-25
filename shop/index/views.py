from django.shortcuts import render
from django.views import generic
from shop.seo.models import Page


class ShopView(generic.View):

    def __init__(self):
        super().__init__()
        self.seo = Page.objects.get_or_create(name=self.page_name)


class IndexView(ShopView):

    def get(self, request):
        context = {'seo': self.seo}
        return render(request, 'index/index.html', context)


