from django.db import models


from django.db import models
from django.shortcuts import reverse


class ProductCategory(models.Model):
    """"""
    img = models.FileField(upload_to='product_category/', blank=True, null=True, verbose_name='Image')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')


class ProductSubcategory(models.Model):
    """"""
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')


class AdditionalCategory(models.Model):
    """"""
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')


class AdditionalCategoryOption(models.Model):
    """"""
    additional_category = models.ForeignKey(AdditionalCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')


class ProductSize(models.Model):
    """"""
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='Name')


class Product(models.Model):
    """"""
    available = models.BooleanField(default=False, verbose_name='Displayed')
    name = models.CharField(max_length=300, blank=True, null=True, verbose_name='Name')
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name='Category')
    subcategory = models.ForeignKey(ProductSubcategory, on_delete=models.SET_NULL, blank=True, null=True,
                                    verbose_name='Subcategory')
    size = models.ManyToManyField(ProductSize, verbose_name='Size')
    additional_category = models.ForeignKey(AdditionalCategory, on_delete=models.SET_NULL,
                                            null=True, blank=True, verbose_name='Tags(additional category')
    description = models.TextField(verbose_name='Description')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])


class ProductImage(models.Model):
    """"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images', related_query_name='images')
    img = models.FileField(upload_to='products/', blank=True, null=True, verbose_name='Image(big)')
    img_mini = models.FileField(upload_to='products/', blank=True, null=True, verbose_name='Image(mini)')



