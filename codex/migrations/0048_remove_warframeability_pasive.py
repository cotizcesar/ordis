# Generated by Django 2.1.4 on 2018-12-12 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0047_auto_20181212_1004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warframeability',
            name='pasive',
        ),
    ]
