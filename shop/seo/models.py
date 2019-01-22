from django.db import models


class Keyword(models.Model):
    name = models.CharField(max_length=150, default='', verbose_name='Ключевое слово страницы')

    class Meta:
        verbose_name = 'Ключевое слово'
        verbose_name_plural = 'Ключевые слова'

    def __str__(self):
        return self.name


class Page(models.Model):
    name = models.CharField(max_length=150, default='', blank=True, verbose_name='Название страницы')

    title = models.CharField(max_length=250, default='', blank=True, verbose_name='Title')
    keywords = models.ManyToManyField(Keyword, blank=True, verbose_name='Ключевые слова')
    description = models.CharField(max_length=500, default='', blank=True, verbose_name='Description')

    raw_html = models.TextField(default='', blank=True, verbose_name='Meta html code')

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.name





