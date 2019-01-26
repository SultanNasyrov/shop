from django.shortcuts import render
from django.views import generic

from shop.seo.models import Page


class ShopBaseView(generic.View):
    """Shop Views Base Class"""

    template_name = None
    page_name = None
    _context = {}

    def get_context(self):
        return self._context

    def change_context(self, request):
        context = self.get_context()
        return context

    def prepare_view(self, request):
        context = self.change_context(request)
        seo, _ = Page.objects.get_or_create(name=self.page_name)
        context['seo'] = seo

    def get(self, request):
        self.prepare_view(request)
        return render(request, self.template_name, self.get_context())




