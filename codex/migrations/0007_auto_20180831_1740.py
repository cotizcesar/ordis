# Generated by Django 2.1 on 2018-08-31 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0006_auto_20180831_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='description',
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='quest',
            name='overview',
            field=models.TextField(max_length=5000, null=True),
        ),
    ]