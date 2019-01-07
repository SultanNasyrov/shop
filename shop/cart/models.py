from django.db import models
from shop.catalog.models import Product


class Cart(models.Model):
    """"""
    total = models.PositiveIntegerField(default=0, verbose_name='Total')


class CartItem(models.Model):
    """"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    subtotal = models.PositiveIntegerField(default=0, verbose_name='Subtotal')

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

    def __str__(self):
        return self.product.name