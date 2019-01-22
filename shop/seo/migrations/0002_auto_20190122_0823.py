# Generated by Django 2.1.5 on 2019-01-22 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150, verbose_name='Ключевое слово страницы')),
            ],
        ),
        migrations.RemoveField(
            model_name='keywords',
            name='page',
        ),
        migrations.DeleteModel(
            name='Keywords',
        ),
        migrations.AddField(
            model_name='page',
            name='keywords',
            field=models.ManyToManyField(blank=True, to='seo.Keyword', verbose_name='Ключевые слова'),
        ),
    ]