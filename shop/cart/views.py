from django.shortcuts import render
from django.views import generic



class CartIndexView(generic.TemplateView):
    page_seo = ''
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        pass





