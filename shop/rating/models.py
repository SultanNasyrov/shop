from django.db import models
from shop.catalog.models import Product


class Rating(models.Model):
    """"""
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='rating', related_query_name='rating')
    likes = models.PositiveIntegerField(default=0, verbose_name='Number of likes')
    views = models.PositiveIntegerField(default=0, verbose_name='Number of view')
    add_to_cart = models.PositiveIntegerField(default=0, verbose_name='Added to cart')
    add_to_wish_list = models.PositiveIntegerField(default=0, verbose_name='Added to wish list')
    purchase = models.PositiveIntegerField(default=0, verbose_name='Purchased')

    def __str__(self):
        return self.product.name

    @property
    def overall
