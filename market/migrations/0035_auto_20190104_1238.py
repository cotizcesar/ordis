# Generated by Django 2.1.4 on 2019-01-04 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0034_auto_20190104_1236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderbeast',
            name='item',
        ),
        migrations.RemoveField(
            model_name='orderbeast',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderBeast',
        ),
    ]
