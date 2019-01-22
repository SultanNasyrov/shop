# Generated by Django 2.1.5 on 2019-01-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keywords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Ключевое слово страницы')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=150, verbose_name='Название страницы')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Description')),
            ],
        ),
        migrations.AddField(
            model_name='keywords',
            name='page',
            field=models.ManyToManyField(to='seo.Page', verbose_name='Страница'),
        ),
    ]
