from django.shortcuts import render, HttpResponse, Http404
from django.views import generic

from shop.core.views import ShopBaseView

from .session_cart import SessionCart, CartItem

import json


class CartIndexView(ShopBaseView):
    page_name = 'Корзина: главная'
    template_name = 'cart/index.html'

    def prepare_context(self, request, args, kwargs):
        pass


def add_item(request):
    if request.method == 'POST' and request.is_ajax():
        product_id, quantity = request.POST['product_id'], request.POST['quantity']
        cart_item = CartItem(product_id, quantity)
        cart = SessionCart(request)
        cart.add(cart_item)
        response = {
        }
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def delete_item(request):
    if request.method == 'POST' and request.is_ajax():
        cart_item = CartItem(request.POST['product_id'])
        cart = SessionCart(request)
        cart.delete(cart_item)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def change_quantity(request):
    if request.method == 'POST' and request.is_ajax():
        product_id, new_quantity = request.POST['product_id'], request.POST['new_quantity']
        cart_item = CartItem(product_id, new_quantity)
        cart = SessionCart(request)
        cart.change_quantity(cart_item)
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404


def clear(request):
    if request.method == 'POST' and request.is_ajax():
        cart = SessionCart(request)
        cart.clear()
        response = {}
        return HttpResponse(json.dumps(response))
    else:
        raise Http404





