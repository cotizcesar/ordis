# Generated by Django 2.1.4 on 2018-12-05 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0037_auto_20181126_1150'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stat',
            options={'ordering': ['-weapon']},
        ),
        migrations.AlterModelOptions(
            name='weapon',
            options={'ordering': ['-name']},
        ),
    ]
