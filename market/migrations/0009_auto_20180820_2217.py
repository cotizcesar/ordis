# Generated by Django 2.1 on 2018-08-21 03:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_auto_20180820_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='component',
            new_name='main',
        ),
    ]
