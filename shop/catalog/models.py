from django.db import models
from django.shortcuts import reverse
from django.template.defaultfilters import slugify


class DisplayedProducts(models.Manager):
    """
    Manager for displayed products

    """
    def get_queryset(self):
        return super().get_queryset().filter(display=True)


class ProductCategory(models.Model):
    """
    Product category

    """
    img = models.FileField(upload_to='product_category/', blank=True, null=True, verbose_name='Изображение')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class ProductSize(models.Model):
    """"""
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Название')

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Продукт"""
    display = models.BooleanField(default=False, verbose_name='Отображается')
    title = models.CharField(max_length=300, blank=True, null=True, verbose_name='Название')
    size = models.ManyToManyField(ProductSize, related_name='sizes', verbose_name='Размер')
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')

    objects = models.Manager()
    displayed = DisplayedProducts()

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    @property
    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('catalog:detail', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    """Изображение продукта"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', related_query_name='images')
    img = models.FileField(upload_to='products/', blank=True, null=True, verbose_name='Изображение(основное)')
    img_mini = models.FileField(upload_to='products/', blank=True, null=True, verbose_name='Изображение(миниматюра)')



