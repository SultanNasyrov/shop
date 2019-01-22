# Generated by Django 2.1.5 on 2019-01-09 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190109_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='additionalcategoryoption',
            name='additional_category',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='productsubcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегории'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='additional_category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.AddField(
            model_name='product',
            name='displayed',
            field=models.BooleanField(default=False, verbose_name='Отображается'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.ProductSubcategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(to='catalog.ProductSize', verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='product_category/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='Изображение(основное)'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='img_mini',
            field=models.FileField(blank=True, null=True, upload_to='products/', verbose_name='Изображение(миниматюра)'),
        ),
        migrations.AlterField(
            model_name='productsize',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='productsubcategory',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='AdditionalCategory',
        ),
        migrations.DeleteModel(
            name='AdditionalCategoryOption',
        ),
    ]