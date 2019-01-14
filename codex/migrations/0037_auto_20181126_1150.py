# Generated by Django 2.1 on 2018-11-26 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0036_auto_20181124_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='trigger',
            field=models.CharField(blank=True, choices=[('T', 'Active'), ('A', 'Auto'), ('B', 'Burst'), ('C', 'Charge'), ('D', 'Duplex'), ('H', 'Held'), ('S', 'Semi')], max_length=1, null=True),
        ),
    ]
