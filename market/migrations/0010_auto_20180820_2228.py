# Generated by Django 2.1 on 2018-08-21 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_auto_20180820_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(),
        ),
    ]
