from django.shortcuts import render, HttpResponse, Http404
from django.views import generic

from .cart import Cart, CartItem


class CartIndexView(generic.TemplateView):
    page_seo = ''
    template_name = 'cart/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request):
        pass


def add_item(request):
    if request.method == 'POST' and request.is_ajax():
        product_id, quantity = request.POST['product_id'], request.POST['quantity']
        cart_item = CartItem(product_id, quantity)
        return HttpResponse()
    else:
        raise Http404





