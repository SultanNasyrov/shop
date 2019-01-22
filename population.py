import os
import django
# set up environment to work with Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')
django.setup()


import random
from PIL import Image
from shop.catalog.models import ProductSize, ProductCategory, ProductSubcategory, Product

FILE_PATH = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(FILE_PATH, 'population/images/')


def get_product_images_list():
    product_images = [os.path.abspath(x) for x in os.listdir(os.path.join(IMAGES, 'product'))]
    return product_images


def get_category_images_list():
    category_images = [os.path.abspath(x) for x in os.listdir(os.path.join(IMAGES, 'category'))]
    return category_images


# CATALOG POPULATION
def populate_sizes():
    sizes = ['XS', 'S', 'M', 'L', 'XL', 'XXL']
    for i in sizes:
        ProductSize.objects.create(name=i)
        print('Размер {} был создан'.format(i))


def populate_categories():

    category_images = get_category_images_list()

    for i in range(4):
        ProductCategory.objects.create(
            img=random.choice(category_images),
            name='Категория {}'.format(i)
        )
        print('Категория {} была создана'.format(i))

    categories = ProductCategory.objects.all()

    for category in categories:
        for i in range(1, random.randrange(5)):
            ProductSubcategory.objects.create(
                category=category,
                name='Подкатегория {}'.format(i)
            )
            print('Подкатегория {} Категории "{}" была создана'.format(i, category.name))


def populate_products():
    product_images = get_product_images_list()
    description = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Vivamus id volutpat quam. Vivamus feugiat elementum dolor ac imperdiet. 
    Morbi magna enim, tincidunt vel nisi in, venenatis congue ligula. 
    Suspendisse augue quam, ornare et ligula et, ultricies vehicula eros. 
    Pellentesque dapibus nisi tortor, eu tincidunt urna sagittis quis. 
    """

    for i in range(30):
        product = Product.objects.create(
            display=True,
            name='Продукт {}'.format(i),
            category=ProductSubcategory.objects.order_by('?').first(),
            description=description
        )
        for image in random.sample(product_images, 2):
            image = Image.open(image)
            product.images.add(image)

        print('Продукт {} был создан'.format(i))


def main():
    populate_sizes()
    populate_categories()
    populate_products()


if __name__ == '__main__':
    main()



