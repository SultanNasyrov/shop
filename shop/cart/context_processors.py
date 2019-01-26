from shop.cart.cart import SessionCart


def cart(request):
    cart = SessionCart(request)
    return {'cart': {'items': cart.items_count, 'total': cart.total}}