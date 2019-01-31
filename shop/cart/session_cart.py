from shop.catalog.models import Product


class CartItem(object):

    def __init__(self, product_id, quantity=1):
        product_inst = Product.objects.get(id=product_id)
        self.product_id = int(product_id)
        self.price = int(product_inst.price)
        self.quantity = int(quantity)
        self.subtotal = self._count_subtotal()

    @property
    def dictionary_name(self):
        return 'Товар {}'.format(self.product_id)

    def _count_subtotal(self):
        return self.price * self.quantity

    def to_dictionary(self):
        dictionary = {
            self.dictionary_name: {
                'product': self.product_id,
                'price': self.price,
                'quantity': self.quantity,
                'subtotal': self.subtotal,
            }
        }
        return dictionary


class SessionCart(object):

    def __init__(self, request):
        self.session = request.session
        if 'cart' in self.session:
            self.cart = self.session['cart']
        else:
            request.session['cart'] = 'cart'

    @property
    def items_count(self):
        return len(self.cart)

    @property
    def total(self):
        total = 0
        for item in self.cart.values():
            total += item['price']
        return total

    def save(self):
        self.session['cart'] = self.cart

    def add(self, cart_item):
        self.cart.update(cart_item.to_dictionary())
        self.save()

    def change_quantity(self, cart_item):
        self.cart[cart_item.dictionary_name]['quantity'] = cart_item.quantity
        self.save()

    def delete(self, cart_item):
        self.cart.pop(cart_item.dictionary_name)
        self.save()

    def clear(self):
        self.cart = {}
        self.save()


