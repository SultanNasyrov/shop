# Generated by Django 2.1.5 on 2019-01-26 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190126_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]