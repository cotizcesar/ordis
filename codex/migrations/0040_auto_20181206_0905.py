# Generated by Django 2.1.4 on 2018-12-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0039_auto_20181205_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='fall_off_end',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='fall_off_start',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='per_stack_end',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='per_stack_start',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weapon',
            name='is_tradeable',
            field=models.BooleanField(default=False),
        ),
    ]
