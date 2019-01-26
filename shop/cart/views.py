from django.shortcuts import render, HttpResponse, Http404
from django.views import generic

from .cart import Cart, CartItem

import json


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
        cart = Cart(request)
        cart.add(cart_item)
        response = {
        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def delete_item(request):
    if request.method == 'POST' and request.is_ajax():
        cart_item = CartItem(request.POST['product_id'])
        cart = Cart(request)
        cart.delete(cart_item)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def change_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        product_id, new_quantity = request.POST['product_id'], request.POST['new_quantity']
        cart_item = CartItem(product_id, new_quantity)
        cart = Cart(request)
        cart.change_quantity(cart_item)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def clear(request):
    if request.method == 'POST' and request.is_ajax():
        cart = Cart(request)
        cart.clear()
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404





