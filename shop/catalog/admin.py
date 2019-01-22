from django.contrib import admin
from .models import (Product, ProductCategory, ProductSize, ProductImage,
                     ProductSubcategory)


class ProductSubcategoryInline(admin.TabularInline):
    model = ProductSubcategory
    extra = 0


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    inlines = [ProductSubcategoryInline]


@admin.register(ProductSize)
class ProductSizeAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


