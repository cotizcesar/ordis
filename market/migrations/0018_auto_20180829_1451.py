# Generated by Django 2.1 on 2018-08-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0017_auto_20180828_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]