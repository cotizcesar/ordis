# Generated by Django 2.1 on 2018-08-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0003_quest_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='slug',
            field=models.SlugField(),
        ),
    ]
