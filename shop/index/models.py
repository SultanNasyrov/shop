from django.db import models


class Banner(models.Model):
    """
    Баннеры карусели
    """
    img = models.FileField(upload_to='carousel/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return 'Баннер {}'.format(self.id)

