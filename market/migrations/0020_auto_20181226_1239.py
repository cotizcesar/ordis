# Generated by Django 2.1.4 on 2018-12-26 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0019_auto_20180829_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='description',
        ),
        migrations.RemoveField(
            model_name='item',
            name='ducats',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.RemoveField(
            model_name='item',
            name='mastery_rank',
        ),
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='item',
            name='rarity',
        ),
        migrations.RemoveField(
            model_name='item',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='item',
            name='trading_tax',
        ),
        migrations.RemoveField(
            model_name='item',
            name='url',
        ),
    ]
