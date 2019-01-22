from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    """"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0, verbose_name='Total')


class CartItem(models.Model):
    """"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Quantity')
    subtotal = models.PositiveIntegerField(default=0, verbose_name='Subtotal')

    class Meta:
        verbose_name = 'Cart item'
        verbose_name_plural = 'Cart items'

    def __str__(self):
        return self.product.name