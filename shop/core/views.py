from django.shortcuts import render, get_object_or_404
from django.views import generic

from shop.seo.models import Page
from shop.catalog.models import Product


class ShopBaseView(generic.View):
    """Shop Views Base Class"""

    template_name = None
    page_name = None
    _context = {}

    def get_context(self):
        return self._context

    def prepare_context(self, request, args, kwargs):
        context = self.get_context()
        return context

    def prepare_seo(self):
        context = self.get_context()
        seo, _ = Page.objects.get_or_create(name=self.page_name)
        context['seo'] = seo

    def get(self, request, *args, **kwargs):
        self.prepare_context(request, args=args, kwargs=kwargs)
        self.prepare_seo()
        return render(request, self.template_name, self.get_context())


class ShopDetailView(ShopBaseView):
    pass





