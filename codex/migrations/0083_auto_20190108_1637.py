# Generated by Django 2.1.4 on 2019-01-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0082_auto_20190108_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itemabilityvalue',
            options={'ordering': ['item', 'name_id']},
        ),
        migrations.AlterModelOptions(
            name='itemattributevalue',
            options={'ordering': ['item']},
        ),
        migrations.AlterField(
            model_name='itemabilityvalue',
            name='value',
            field=models.TextField(max_length=210),
        ),
    ]
