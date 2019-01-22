from django.db import models
from django.contrib.auth.models import User

from shop.catalog.models import Product


class RecentlyViewed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='recently_viewed')

    class Meta:
        verbose_name = 'Recently viewed'
        verbose_name_plural = 'Recently viewed'

    def __str__(self):
        return 'Recently viewed'
