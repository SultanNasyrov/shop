from django.db import models

from django.contrib.auth.models import User


class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Wish list'
        verbose_name_plural = 'Wish list'

    def __str__(self):
        return 'Wish list'
