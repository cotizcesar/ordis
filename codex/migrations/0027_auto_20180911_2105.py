# Generated by Django 2.1 on 2018-09-12 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0026_auto_20180911_1840'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quest',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ['tipe']},
        ),
        migrations.AlterModelOptions(
            name='weapon',
            options={'ordering': ['name']},
        ),
    ]
