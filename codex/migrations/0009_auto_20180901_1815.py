# Generated by Django 2.1 on 2018-09-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0008_auto_20180901_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]
