from shop.catalog.models import Product


class CartItem(object):
    def __init__(self, product_id, quantity):
        product_inst = Product.objects.get(id=product_id)
        self.product = int(product_id)
        self.price = int(product_inst.price)
        self.quantity = int(quantity)
        self.subtotal = self._count_subtotal()

    @property
    def dictionary_name(self):
        return 'Товар {}'.format(self.product)

    def _count_subtotal(self):
        return self.price * self.quantity

    def to_dictionary(self):
        dictionary = {
            self.dictionary_name: {
                'product': self.product,
                'price': self.price,
                'quantity': self.quantity,
                'subtotal': self.subtotal,
            }
        }
        return dictionary


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        if 'cart' in self.session:
            self.cart = self.session['cart']
        else:
            request.session['cart'] = 'cart'

    def save(self):
        self.session['cart'] = self.cart

    def add_item(self, cart_item):
        self.cart.update(cart_item.to_dictionary())
        self.save()

    def clear(self):
        self.cart = {}
        self.save()





