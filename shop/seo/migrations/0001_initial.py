# Generated by Django 2.1.5 on 2019-01-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Ключевое слово страницы')),
            ],
            options={
                'verbose_name': 'Ключевое слово',
                'verbose_name_plural': 'Ключевые слова',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=150, verbose_name='Название страницы')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Title')),
                ('description', models.CharField(blank=True, default='', max_length=500, verbose_name='Description')),
                ('raw_html', models.TextField(blank=True, default='', verbose_name='Meta html code')),
                ('keywords', models.ManyToManyField(blank=True, to='seo.Keyword', verbose_name='Ключевые слова')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
