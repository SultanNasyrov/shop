from django.db import models
from shop.catalog.models import Product


class RecentlyViewed(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Recently viewed'
        verbose_name_plural = 'Recently viewed'

    def __str__(self):
        return 'Recently viewed'
